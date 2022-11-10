# paint_calculator
This is paint calculator, it will calculate the paint based on given length, width and height. There are some assumption made based on requirement of the programme, please read this file.

In this programmes there are some assumption made based on requirement of the programme to give more efficient results.
Here, I have assumed that,
        THICKNESS = 0.1  #assumed that thickness of wall is 0.1m
        SPREADING_RATE = 10  #assumed that spearding rate is 10 metre square per litre
        NUMBER_OF_COAT = 1  #assumed that 1 coating of paint
        WINDOW_LENGTH = 1.5  # assumed that windows length is 1 meter
        WINDOW_HEIGHT = 2  # assumed that windows height is 2 meter
        DOOR_LENGTH = 1  #assumed that doors length is 1 meter
        DOOR_HEIGHT = 3 # assumed that doors height is 3 meter
        
As rooms can be in any shapes, so here, I made assumption that in this ROOM is in cubical shape.
This programme takes 3 arguments and then initialise it into 3 variables, holding value of length of room, width of room and height of room.
Then I am getting area of floor, which is rectangle using 'get_area_of_floor' function, getting area of windows where there is assumption of length and width, using 'get_area_of_windows' function, getting area of doors, again there is some assumption of length and width using 'get_are_of_door' function,getting required paint for the 1 coat only using 'get_required_paint' function and lastly I am getting volumn of the room, where room is cubical, using 'get_volume_of_room' function.

Then, I have imported the the library called unittest, for unit testing of the code.

In unit testing I am testing area of floor using 'test_get_area_of_floor' function, area of windows using 'test_area_of_windows' function, area of door using 'test_area_of_door' function, testing required quantity of paint using 'test_get_required_paint' function and at last I am testing volumn of the room using 'test_get_volume_of_room' function.

Now if I talk about main function then, I have prompt user to input value of length, width and height, by which we calculate all the required mesuremnt and will out based on it. Once the calculation is finished user will se value of Area of floor (in metre square), Quantity of required paint (in litres) and Volume of room (in cubic metre). 

Then finally all test cases will run and programme will over.

Bingo!!!
