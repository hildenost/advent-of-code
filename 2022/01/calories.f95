program day01
  use utils, only: readinput
  implicit none

  ! Problem related variables
  character, dimension(:,:), allocatable :: scanning

  call readinput(scanning, day="01", cols=1)

  print *, scanning

end program day01
