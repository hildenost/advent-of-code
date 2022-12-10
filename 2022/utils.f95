module utils
  implicit none
  
  private

  public :: readinput

contains


  subroutine readinput(content, day, cols)
    ! Signature variables 
    character, dimension(:,:), allocatable, intent(inout) :: content
    character(2), intent(in) :: day
    integer, optional :: cols

    ! Internal parameters
    integer           :: i

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0

    ! If there is a columns variable, the incrementation of length
    ! must be that number
    if (present(cols)) then
      i = cols
    else
      i = 1
    endif

    ! Fortran needs to know how large the array is going to be
    ! before allocating
    ! First we do a pass over the input file to count number of lines
    open(newunit=io, file=day//"/input.txt", status="old", action="read")
    do
        read(io, *, iostat=iostat)
        if (is_iostat_end(iostat)) exit
        length = length + 1
    end do
    ! Now we can allocate our file contents array
    allocate(content(i, length))

    ! And finally, we can store the input in the array
    rewind(io)
    read(io, *) content
    close(io)
  end subroutine readinput


end module utils
