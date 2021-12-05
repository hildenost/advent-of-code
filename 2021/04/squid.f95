program day04
    implicit none

    ! Variables related to file I/O
    integer :: io

    ! Problem related variables
    integer, parameter :: N = 100 ! number of numbers
                                  ! and also number of boards
    integer, parameter :: board_size = 25

    integer, dimension(N*board_size) :: boards 
    logical, dimension(N*board_size) :: mask

    integer, dimension(N) :: numbers
    logical, dimension(N) :: win_mask

    integer :: i
    integer :: j

    ! External functions type declaration
    logical :: check_board
    integer :: findidx

    ! Today, we know the sizes of the arrays
    open(newunit=io, file="input.txt", status="old", action="read")
    read(io, *) numbers, boards
    close(io)

    
    do i=1,N
      ! Adding to mask more drawn numbers
      mask = mask .or. boards == numbers(i)

      ! For Part 2
      ! If only one board that hasn't won left
      if (count(win_mask) == N - 1) then
        j = findidx(win_mask, .False., N)
        print *, "PART 2", answer(j, numbers(i))
        ! Then we're completely done
        exit
      end if

      win_mask = [(check_board(select_mask(i)), i=1, N)]

      ! For Part 1
      ! If only one board has won
      if (count(win_mask) == 1) then
        j = findidx(win_mask, .True., N)
        print *, "PART 1", answer(j, numbers(i))
      end if
    end do

contains
  ! Internal functions inherits scope

  pure function answer(start, num) result(res)
    integer, intent(in) :: start
    integer, intent(in) :: num
    integer :: res
    
    res = num * sum(pack(select_board(j), .not. select_mask(j)))

  end function answer

  pure function select_board(start) result(board)
    integer, intent(in) :: start
    integer, dimension(board_size) :: board

    board = boards((start-1)*board_size + 1:start*board_size)
  end function select_board

  pure function select_mask(start) result(board)
    integer, intent(in) :: start
    logical, dimension(board_size) :: board

    board = mask((start-1)*board_size + 1:start*board_size)
  end function select_mask

end program day04


pure function findidx(arr, value, n) result(idx)
  integer, intent(in) :: n
  logical, dimension(n), intent(in) :: arr
  logical, intent(in) :: value
  integer :: idx

  do idx=1, n
    if (arr(idx) .eqv. value) then
      exit
    end if
  end do

end function findidx

pure function check_board(board) result(bingo)
  logical, dimension(5, 5), intent(in) :: board
  logical :: bingo

  bingo = any(count(board, dim=1) == 5) .or. any(count(board, dim=2) == 5)

end function check_board

