program day01
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0

    ! Problem related variables
    character*256, dimension(:), allocatable :: scanning
    integer :: dial = 50
    integer :: password = 0


    ! Fortran needs to know how large the array is going to be
    ! before allocating
    ! First we do a pass over the input file to count number of lines
    open(newunit=io, file="input.txt", status="old", action="read")
    do
        read(io, *, iostat=iostat) 
        if (is_iostat_end(iostat)) exit
        length = length + 1
    end do
    ! Now we can allocate our scanning array
    allocate(scanning(length))
    ! And finally, we can store the input in the array
    rewind(io)
    read(io, *) scanning
    close(io)


    call part1(scanning)

    write (*,*) "Part 1", password

  contains

    impure elemental subroutine part1(rotation)
      implicit none

      character*256, intent(in) :: rotation

      character :: dir
      integer :: steps

      dir = rotation(1:1)
      ! convert the rest of the string to an integer
      read(rotation(2:), *) steps

      ! This block can be replaced by merge(),
      ! but the if block is more readable
      if (dir == "L") then
        dial = dial - steps
      else
        dial = dial + steps
      end if
      dial = modulo(dial, 100)

      if (dial == 0) then
        password = password + 1
      end if
      
    end subroutine part1
end program day01
