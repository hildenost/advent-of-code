program day02
  use utils, only: readinput
  implicit none

  ! Problem related variables
  character, dimension(:,:), allocatable :: scanning

  call readinput(scanning, day="02", cols=2)

  write (*,*) "Part 1", sum(score1(scanning(1,:), scanning(2,:)))
  write (*,*) "Part 2", sum(score2(scanning(1,:), scanning(2,:)))

contains

  pure elemental function score1(opponent, me) result(score)
    character, intent(in) :: opponent
    character, intent(in) :: me
    integer               :: score

    select case (ichar(me)-ichar(opponent))
    ! If equal, me-opp = 23
      case (23)
        score = 3
    ! If I win, me-opp = 24 or 21
      case (21, 24)
        score = 6
    ! If I lose, me-opp= 25 or 22
      case (22, 25)
        score = 0
    end select

    score = score + ichar(me) - 87
  end function

  pure elemental function score2(opponent, res) result(score)
    character, intent(in) :: opponent
    character, intent(in) :: res 
    integer               :: oppchoice
    integer               :: score

    oppchoice = ichar(opponent) - 65

    select case (res)
    ! If res = X, aim for lose
      case ("X")
        score = 0 + modulo(oppchoice - 1, 3) + 1  
    ! If res = Y, aim for draw
      case ("Y")
        score = 3 + oppchoice + 1 
    ! If res = Z, aim for win 
      case ("Z")
        score = 6 + modulo(oppchoice + 1, 3) + 1
    end select

  end function

end program day02
