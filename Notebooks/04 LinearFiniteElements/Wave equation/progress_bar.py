import sys, time, queue
from typing import Any
from IPython.display import clear_output


class ProgressBarHandler:
    
    def __init__(self, end_tick: int, title: str = None, zero_starting: bool = True, bar_length: int = 20, remain_after_finish: bool = True) -> None:
        self.end_tick = end_tick
        self.zero_starting = zero_starting
        self.bar_length = bar_length
        self.title = title
        self.remain_after_finish = remain_after_finish

        self.last_time = None
        self.last_tick = 0
        
    def __call__(self, current_tick: int, *args: Any, **kwds: Any) -> Any:
        if self.zero_starting:
            current_tick += 1
            
        if current_tick >= self.end_tick:
            if not self.remain_after_finish:
                clear_output(wait=True)
                return
            
            line = ('[{}] {:.2f}% {}/{} '+' '*10).format('█' * self.bar_length, 100, self.end_tick, self.end_tick)
            if self.title:
                line = self.title + '\n' + line
            clear_output(wait=True)
            time.sleep(0.1)
            sys.stdout.write(line)
            sys.stdout.flush()
            print()
            return

        if self.last_time is None:
            self.last_time = time.time()
            self.last_tick = current_tick
            return
        
        current_time = time.time()
        time_per_tick = (current_time - self.last_time) / (current_tick - self.last_tick) if current_tick > self.last_tick else 0

        if time_per_tick * (current_tick - self.last_tick) < 0.1:
            return
        
        self.last_time = current_time
        self.last_tick = current_tick       
        
        progress = current_tick / self.end_tick
        progress_bar = '█' * int(progress * self.bar_length) + '.' * (self.bar_length - int(progress * self.bar_length))
        percentage = min(progress * 100, 100)
        etr = (self.end_tick - current_tick) * time_per_tick
                
        line = '[{}] {:.2f}% {}/{} {}'.format(progress_bar, percentage, min(current_tick, self.end_tick), self.end_tick, time.strftime("%H:%M:%S", time.gmtime(etr)))
        clear_output(wait=False)
        if self.title:
            line = self.title + '\n' + line
        sys.stdout.write(line)
        sys.stdout.flush()
        

if __name__ == '__main__':
    bar_handler = ProgressBarHandler(int(1e6))
    
    for i in range(int(1e6)):
        bar_handler(i)
        time.sleep(1e-5)