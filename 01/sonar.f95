program day01
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0
    integer :: i

    ! Problem related variables
    integer, dimension(:), allocatable :: scanning
    ! size of sliding window
    integer :: k


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
    ! We could do the magic that was the task while looping
    ! but we want to make this file I/O a module for future use
    rewind(io)
    do i = 1, length ! Arrays start at 1!!!!! DON'T @ ME
        read(io, *) scanning(i)
    end do
    close(io)


    ! In part 2, we are comparing whether a + b + c < b + c + d
    ! which simplifies to comparing a < d 
    ! The solution can therefore be generalized as a function of
    ! sliding window size k
    do k = 1, 3, 2  ! start, stop, step
        ! [(statement, i=start, stop(, step))] is an implicit do loop
        ! COUNT is an intrinsic function that counts the number of .TRUE.
        ! elements in a Boolean array
        write(*, *) count([(scanning(i) > scanning(i-k), i=k+1, size(scanning))])
    end do

end program day01