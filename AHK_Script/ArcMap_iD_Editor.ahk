#Requires AutoHotkey v2.0
SetTitleMatchMode(2)

; ==========================================
; 1. SHORTCUT UTAMA ARCMAP
; ==========================================
#HotIf WinActive("ArcMap")
Space::Click()

; Menerjemahkan angka tunggal ke shortcut kombinasi ArcMap
1::Send("^1") ; Ctrl+1 untuk Select Features
2::Send("^2") ; Ctrl+2 untuk Cut Polygons
3::Send("^3") ; Ctrl+3 untuk Clear Selection
w::Send("^w") ; Ctrl+W untuk Toggle Top Layer
+s::Send("^+s") ; Shift+S diterjemahkan jadi Ctrl+Shift+S (Save Edits)
#HotIf

; ==========================================
; 2. JENDELA MERGE (Navigasi & Flash)
; ==========================================
#HotIf WinActive("Merge ahk_exe ArcMap.exe")
; Turun dan trigger "Space" agar poligon patokan berkedip (Flash)
^q::Send("{Down}{Space}")

; Shift+Q untuk naik ke atas (mengatasi list mentok di bawah)
+q::Send("{Up}{Space}")
#HotIf
