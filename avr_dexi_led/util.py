from threading import Event as _Event

from adafruit_led_animation.animation import Animation as _Animation


def run_anim_until_done(anim: _Animation) -> None:
    event = _Event()
    anim.add_cycle_complete_receiver(lambda _: event.set())
    while not event.is_set():
        anim.animate()
