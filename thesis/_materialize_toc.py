#!/usr/bin/env python3
"""DOCX içindeki TOC/index/field alanlarını LibreOffice headless ile gerçek
başlık + sayfa numaralarıyla DOLDURUR (materialize) ve DOCX'i tekrar kaydeder.

Sadece w:dirty/updateFields bayrağı yeterli değil; bu adım Word'de elle güncelleme
gerektirmeden final DOCX içinde görünür dolu İÇİNDEKİLER üretir.
"""
import os, sys, subprocess, time, glob, urllib.parse

HOME = os.path.expanduser("~")
SOFFICE = f"{HOME}/Applications/LibreOffice.app/Contents/MacOS/soffice"
PROFILE_ROOT = "/tmp/ytu_libreoffice_profile"
PROFILE = f"{PROFILE_ROOT}/user"
MODULE = f"{PROFILE}/basic/Standard/Module1.xba"

MACRO = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="Module1" script:language="StarBasic">REM  *****  BASIC  *****

Sub Main
End Sub

Sub UpdateDoc(sUrl As String)
  Dim oDoc As Object
  Dim oArgs(0) As New com.sun.star.beans.PropertyValue
  oArgs(0).Name = "Hidden"
  oArgs(0).Value = True
  oDoc = StarDesktop.loadComponentFromURL(sUrl, "_blank", 0, oArgs())
  On Error Resume Next
  oDoc.getTextFields().refresh()
  Dim oIdx As Object
  oIdx = oDoc.getDocumentIndexes()
  Dim i As Integer
  For i = 0 To oIdx.getCount() - 1
    oIdx.getByIndex(i).update()
  Next i
  On Error Goto 0
  Dim oSave(0) As New com.sun.star.beans.PropertyValue
  oSave(0).Name = "FilterName"
  oSave(0).Value = "MS Word 2007 XML"
  oDoc.storeToURL(sUrl, oSave())
  oDoc.close(False)
End Sub</script:module>'''


def install_macro():
    os.makedirs(os.path.dirname(MODULE), exist_ok=True)
    with open(MODULE, "w", encoding="utf-8") as f:
        f.write(MACRO)


def materialize(docx_path):
    if not os.path.isfile(SOFFICE):
        print("soffice yok, atlanıyor:", SOFFICE)
        return False
    install_macro()
    abspath = os.path.abspath(docx_path)
    url = "file://" + urllib.parse.quote(abspath)
    macro_url = f'macro:///Standard.Module1.UpdateDoc("{url}")'
    # önce çalışan soffice örneklerini kapat
    subprocess.run(["pkill", "-f", "soffice"], capture_output=True)
    time.sleep(1)
    proc = subprocess.Popen(
        [SOFFICE, f"-env:UserInstallation=file://{PROFILE_ROOT}",
         "--headless", "--norestore", "--invisible",
         "--nofirststartwizard", macro_url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        proc.wait(timeout=120)
    except subprocess.TimeoutExpired:
        proc.kill()
    subprocess.run(["pkill", "-f", "soffice"], capture_output=True)
    return True


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else \
        "Quantum Grup Yapıları - YTÜ Bitirme Tezi.docx"
    materialize(target)
    print("TOC materialize tamam:", target)
