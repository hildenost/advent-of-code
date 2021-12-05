program day04
    implicit none

    ! Variables related to file I/O
    integer :: iostat
    integer :: io
    integer :: length = 0
    integer :: values_per_line = 1 

    ! Problem related variables
    integer, parameter :: N = 100 ! number of numbers
                                  ! and also number of boards
    integer, parameter :: board_size = 25
    integer, dimension(N*board_size) :: boards 
    logical, dimension(N*board_size) :: mask
    logical, dimension(N) :: win_mask
    character(100) :: line

    integer, dimension(N) :: numbers

    logical :: check_board
    logical :: bingo
    logical :: first

    integer :: i
    integer :: j

    ! Today, we know the sizes of the arrays
    open(newunit=io, file="input.txt", status="old", action="read")
    read(io, *) numbers, boards
    close(io)

    
    do i=1,N
      mask = mask .or. boards == numbers(i)
      if (count(win_mask) == N - 1) then
        do j=1, N
          if (.not. win_mask(j)) then
            exit
          end if
        end do
        win_mask = [(check_board(mask((j-1)*board_size+1:j*board_size)), j=1, N)]
        print *, "PART 2"
        print *, numbers(i) * sum(pack(boards((j-1)*board_size + 1:j*board_size), .not. mask((j-1)*board_size + 1:j*board_size)))
        exit
      end if

      win_mask = [(check_board(mask((j-1)*board_size+1:j*board_size)), j=1, N)]
      if (any(win_mask) .and. .not. first) then
        first = .True.
        do j=1, N
          if (win_mask(j)) then
            exit
          end if
        end do

        print *, "PART 1"
        print *, numbers(i) * sum(pack(boards((j-1)*board_size + 1:j*board_size), .not. mask((j-1)*board_size + 1:j*board_size)))
      end if
    end do

end program day04

pure function check_board(board) result(bingo)
  logical, dimension(5, 5), intent(in) :: board
  logical :: bingo

  bingo = any(count(board, dim=1) == 5) .or. any(count(board, dim=2) == 5)

end function check_board

