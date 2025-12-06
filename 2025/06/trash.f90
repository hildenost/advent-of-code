program day03
    use iso_fortran_env
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0

    ! Problem related variables
    character(3800), dimension(:), allocatable :: lines
    character, dimension(:), allocatable :: temp_ops 
    character, dimension(:), allocatable :: ops 

    integer(kind=selected_int_kind(10)) :: grand_total
    ! Iterator
    integer :: m
    integer :: n

    ! Part 1 related variables
    integer(kind=selected_int_kind(10)), dimension(:, :), allocatable :: part1
    ! Part 2 related variables
    integer(kind=selected_int_kind(10)) :: temp_sum
    integer(kind=selected_int_kind(10)) :: temp_prod
    character, dimension(:, :), allocatable :: test
    character, dimension(:, :), allocatable :: test_t
    character(len=:), allocatable :: temp_string
    integer :: temp_int
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
    allocate(lines(length))
    ! And finally, we can store the input in the array
    rewind(io)
    read(io, '(a)') lines
    close(io)

    ! First, let us find the number of equations
    ! by counting the operators
    temp_ops = string2char(lines(length))
    n = count(temp_ops=="+" .or. temp_ops=="*")

    ! Then, we can allocate our arrays 
    allocate(part1(n, length-1))
    allocate(ops(n))
    ! And read them to their respective variables
    ! We can slice the first lines to just take the length - 1
    ! first lines, but it will be done automatically
    ! because of the target arrays' dimension
    read(lines, *) part1
    read(lines(length), *) ops

    ! PART 1 solve
    grand_total = 0
    do m = 1, n
      if (ops(m) == "+") then
        grand_total = grand_total + sum(part1(m, :))
      else if (ops(m) == "*") then
        grand_total = grand_total + product(part1(m, :))
      end if
    end do

    write(*,*) "Part 1: ", grand_total

    ! PART 2 solve
    ! Need to create char arrays for all lines
    allocate(test(length-1, 3800))
    do m = 1, length-1
      test(m, :) = string2char(lines(m))
    end do
    ! Then we transpose 
    test_t = transpose(test)

    grand_total = 0
    ! To keep track of the equation numbers
    k = 1
    temp_sum = 0
    temp_prod = 1
    do m = 1, 3800
      ! Convert back to string
      temp_string = char2string(test_t(m ,:))
      ! Check if this is a number
      if (len_trim(temp_string) > 0) then 
        ! Convert it to integer
        read(temp_string, *) temp_int
        ! And do the math
        if (ops(k) == "+") then
          temp_sum = temp_sum + temp_int
        else if (ops(k) == "*") then
          temp_prod = temp_prod * temp_int
        end if
      else
        ! Update the total score
        grand_total = grand_total + temp_sum
        if (temp_prod > 1) then
          grand_total = grand_total + temp_prod
        end if

        ! And update the counters
        k = k+1
        temp_sum = 0
        temp_prod = 1
      end if
    end do
    write(*,*) "Part 2: ", grand_total

  contains

    pure function char2string(chars) result (string)
      character, dimension(:), intent(in) :: chars
      integer :: i
      character(len=:), allocatable :: string

      allocate(character(size(chars)) :: string)

      do i = 1, size(chars)
        string(i:i) = chars(i)
      end do

    end function char2string

    pure function string2char(string)  RESULT (array)

    character(len=*),intent(in)     :: string
    character :: array(len(string))
    integer :: i

     do i = 1,size(array)
        array(i) = string(i:i)
     enddo
    end function string2char



end program day03
