#NoEnv

SetBatchLines -1

Process Priority,,R



BlockInput Mouse        ; user mouse input is ignored during MouseMove

CoordMode Mouse, Screen ; absolute coordinates

SysGet m, Monitor       ; get the screen edges

mLeft += 1, mRight -= 2, mTop += 1, mBottom -= 2

SetMouseDelay -1        ; fastest action



MouseGetPos x0, y0      ; get initial mouse pointer location

SetTimer WatchMouse, 1  ; run the subroutine fast (10..16ms)

Return



WatchMouse:

   MouseGetPos x, y     ; get current mouse position

   x0 += 2*(x0-x), x0 := x0 < mLeft ? mLeft : (x0 > mRight  ? mRight  : x0)

   y0 += 2*(y0-y), y0 := y0 < mTop  ? mTop  : (y0 > mBottom ? mBottom : y0)

   MouseMove x0, y0, 0  ; set new position as old, for the next timer

Return



!z::ExitApp             ; stop the madness; make the script persistent