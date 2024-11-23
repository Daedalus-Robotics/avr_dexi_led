from adafruit_led_animation.animation import Animation

class Alternate(Animation):

    def __init__(self, pixel_object, speed, color_a, color_b):
        super().__init__(pixel_object, speed, color_a, color_b)

        self.color_a = color_a
        self.color_b = color_b
        self._tick = 0
        self._tick_end = 4

    def draw(self):
        if self._tick%2 == 0:
            try:
                # Selects even item and sets it to Color A
                self.pixel_object[::2] = [self.color_a]*(len(self.pixel_object)//2)
                # Selects odd item and sets it to Color B
                self.pixel_object[1::2] = [self.color_b]*(len(self.pixel_object)//2)
            except IndexError:
                pass
        else:
            self.pixel_object.fill((0,0,0))

        if self._tick > self._tick_end:
            # call internal reset() function
            self.reset()

        self._tick+=1
    def reset(self):
        self.pixel_object.fill((0,0,0))
        self._tick = 0
