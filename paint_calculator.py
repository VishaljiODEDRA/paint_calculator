#here, I made assumption that room is in cubical shape

class PaintCalculator():
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.THICKNESS = 0.1  #assumed that thickness of wall is 0.1m
        self.SPREADING_RATE = 10  #assumed that spearding rate is 10 metre square per litre
        self.NUMBER_OF_COAT = 1  #assumed that 1 coating of paint
        self.WINDOW_LENGTH = 1.5  # assumed that windows length is 1 meter
        self.WINDOW_HEIGHT = 2  # assumed that windows height is 2 meter
        self.DOOR_LENGTH = 1  #assumed that doors length is 1 meter
        self.DOOR_HEIGHT = 3  # assumed that doors height is 3 meter

    def get_area_of_floor(self):
        #floor will be rectangle
        return self.width * self.length

    def get_area_of_windows(self):
        #assumed that 2 windows, and having 2 sides, so multiply by 4
        return 4 * (self.WINDOW_LENGTH * self.WINDOW_HEIGHT)

    def get_are_of_door(self):
        #assumed that 1 door, and having 2 sides, so multiply by 2
        return 2 * (self.DOOR_LENGTH * self.DOOR_HEIGHT)

    def get_required_paint(self):
        #total walls = 4, both sides so multiply by 2
        #area of verticles walls
        vertical_inner_walls = 2 * (self.height * (self.length - 2 *
                                                   (self.THICKNESS)))
        vertical_outer_walls = 2 * (self.height * self.length)

        #area of horizantal walls
        horizantal_inner_walls = 2 * (self.height * (self.width - 2 *
                                                     (self.THICKNESS)))
        horizantal_outer_walls = 2 * (self.height * self.width)

        total_area = vertical_inner_walls + vertical_outer_walls + horizantal_inner_walls + horizantal_outer_walls - self.get_are_of_door(
        ) - self.get_area_of_windows()

        required_paint = (total_area /
                          self.SPREADING_RATE) * self.NUMBER_OF_COAT
        return required_paint

    def get_volume_of_room(self):
        #the room will be in shape of cube
        return self.width * self.length * self.height

        
