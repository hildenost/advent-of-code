program day03
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0
    integer :: values_per_line = 1

    ! Problem related variables
    integer, parameter :: n = 12
    integer, dimension(:, :), allocatable :: scanning
    character(n) :: line
    logical, dimension(n) :: mask 

    integer :: i
    integer :: j 
    integer, dimension(:), allocatable :: k

    integer :: gamma
    integer :: epsilon

    integer :: compute_rate



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
    allocate(scanning(length, n))
    allocate(k(length))
    ! And finally, we can store the input in the array
    rewind(io)
    do i = 1, length
        read(io, *) line
        read (line, "(B12)") k(i)

        do j = 1, n
            read(line(j:j), *) scanning(i, j)
        end do
    end do
    close(io)

    !mask = sum(scanning, dim=1) > length / 2

    mask = [(2 * count(btest(k, i)) > length, i=n-1, 0, -1)]

    gamma = compute_rate(mask, n)
    epsilon = compute_rate(.not. mask, n)

    print *, gamma * epsilon

end program day03

pure function compute_rate(mask, n) result(rate)
    logical, dimension(n), intent(in) :: mask 
    integer, intent(in) :: n

    integer, dimension(n) :: int_mask
    character(n) :: binary

    integer :: rate

    ! Convert mask to integer array
    int_mask = transfer(mask, int_mask)
    ! Convert integer array to string
    do i=1, n
        write(binary(i:i), "(I1)") int_mask(i)
    end do
    ! Convert to integer
    read (binary, "(B12)") rate

end function compute_rate