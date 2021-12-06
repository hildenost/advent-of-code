program day04
    implicit none

    ! Variables related to file I/O
    integer :: io

    ! Problem related variables
    integer, dimension(300) :: start_fish
    integer, parameter :: long_int = selected_int_kind(12)
    integer(kind=long_int), dimension(10) :: fish
    integer(kind=long_int) :: spawned_fish

    integer :: i
    integer :: day

    open(newunit=io, file="input.txt", status="old", action="read")
    read(io, *) start_fish
    close(io)

    ! Initializing the fish status counts
    fish = [(count(start_fish == i), i=1, 10)]

    do day=1, 256 
        ! Saving the number of spawning fish
        spawned_fish = fish(10)
        ! Index 10 is reserved for spawning fish
        ! Moving the 1 day left fish to be spawning next day
        fish(10) = fish(1)
        ! Moving the other fish one day up
        fish(1:7) = fish(2:8)

        ! Adding the spawned fish
        fish(8) = spawned_fish
        ! And resetting the counter for the spawning fish
        fish(6) = fish(6) + spawned_fish

        if (day == 80) then
            write (*,*) "Part 1", sum(fish)
        end if
    end do

    write (*,*) "Part 2", sum(fish)

end program day04