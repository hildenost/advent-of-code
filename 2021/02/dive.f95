program day02
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0
    integer :: values_per_line = 2

    ! Problem related variables
    character(30), dimension(:), allocatable :: commands
    integer :: depth = 0
    integer :: pos = 0
    integer :: aim = 0
    integer :: x

    integer :: i


    ! Fortran needs to know how large the array is going to be
    ! before allocating
    ! First we do a pass over the input file to count number of lines
    open(newunit=io, file="input.txt", status="old", action="read")
    do
        read(io, *, iostat=iostat) 
        if (is_iostat_end(iostat)) exit
        length = length + values_per_line
    end do
    ! Now we can allocate our scanning array
    allocate(commands(length))
    ! And finally, we can store the input in the array
    rewind(io)
    read(io, *) commands 
    close(io)


    ! The array commands now contain the commands name at 1, 3, 5, ...
    ! and the X values are at 2, 4, 6 
    do i = 1, length, 2 
        ! Convert to integer
        read(commands(i + 1), * ) x
        select case (commands(i))
            case("forward")
                pos = pos + x 
            case("up")
                depth = depth - x
            case("down")
                depth = depth + x
        end select
    end do

    write(*,*) pos * depth

    depth = 0
    pos = 0
    aim = 0
    ! The array commands now contain the commands name at 1, 3, 5, ...
    ! and the X values are at 2, 4, 6 
    do i = 1, length, 2 
        ! Convert to integer
        read(commands(i + 1), * ) x
        select case (commands(i))
            case("forward")
                pos = pos + x 
                depth = depth + aim * x
            case("up")
                aim = aim - x 
            case("down")
                aim = aim + x 
        end select
    end do

    write(*,*) pos * depth

end program day02