program day01
    implicit none

    integer :: iostat
    integer :: io

    integer, dimension(:), allocatable :: scanning
    logical, dimension(:), allocatable :: mask

    ! size of sliding window
    integer :: k = 3

    integer :: length = 0

    integer :: i


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
    ! We don't have to allocate the other arrays yet, since
    ! their size will be known when doing the implicit loops

    ! And finally, we can store the input in the array
    ! We could do the magic that was the task while looping
    ! but we want to make this file I/O a module for future use
    rewind(io)
    do i = 1, length ! Arrays start at 1!!!!! DON'T @ ME
        read(io, *) scanning(i)
    end do
    close(io)

    ! Part 1
    mask = [(scanning(i) > scanning(i-1), i=2, size(scanning))]
    ! COUNT is an intrinsic function that counts the number of .TRUE.
    ! elements in an array
    write (*,*) count(mask)

    ! Part 2
    ! Creating the rolling sum
    scanning = [(sum(scanning(i-k+1:i)), i=k, size(scanning))]

    mask = [(scanning(i) > scanning(i-1), i=2, size(scanning))]
    write (*,*) count(mask)

end program day01