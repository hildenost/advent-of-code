program day03
    use iso_fortran_env
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0

    ! Problem related variables
    character(len=256), dimension(:), allocatable :: scanning
    integer :: n = 2
    integer(kind=selected_int_kind(16)) :: password

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

    password = sum(max_joltage(scanning, 2))

    write (*,*) "Part 1", password

    password = sum(max_joltage(scanning, 12))

    write (*,*) "Part 2", password

  contains

    integer(kind=int64) elemental function max_joltage(rotation, number) result(intres)
      character(len=*), intent(in) :: rotation
      integer, intent(in) :: number
      character(len=number) :: res

      res = find_largest(trim(rotation), number)

      ! Converting to integer
      read(res, *) intres 

    end function max_joltage 


    pure recursive function find_largest(batteries, number) result(a)
    ! Finds the largest joltage consisting of number batteries
    ! from the batteries configuration
      character(len=*), intent(in) :: batteries
      integer, intent(in) :: number
      character(len=number) :: a

      character :: m
      integer :: idx
      integer :: remaining

      m = maxvalue(batteries)
      idx = index(batteries, m)
      remaining = len(batteries(idx:))

      if (number == 1) then
        a = m 
      else if (number <= remaining) then
        a = m // find_largest(batteries(idx+1:),number - 1)
      else
        a =find_largest(batteries(:idx-1),number-remaining) // batteries(idx:)
      end if

    end function find_largest


    character pure function maxvalue(string) result(m)
      ! Searches a string for digits 1-9, returning
      ! the larges occuring digit.
      character(len=*), intent(in) :: string

      character :: c
      integer :: i

      do i = 9,1,-1
        ! Converting integer to char
        write(c, '(i1)') i

        if (index(string,c) > 0) then
          ! We have found the max value
          ! Exit and be happy
          m = c
          exit
        end if
        
      end do

    end function maxvalue

end program day03
