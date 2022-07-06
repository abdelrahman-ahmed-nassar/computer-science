import queue

# بتعمل طابور من المعلومات واللي بيتشال أول واحد هو اللي بيكون أول واحد إتحط بمعني 

#  FIFO 
# first in , first out 

q = queue.Queue()# ممكن تجط فالقوس عدد العناصر اللي تقدر تحطها بمعني أنك تحدد بدل ما تسبها مفتوحه
q.empty()# if the queue is empty or not 
q.put("item1")# putting items in the queue 
q.put("item2")
q.put("item3")

q.get()# give you the item1 
q.get()# give you the item2
q.get()

# ممكن تفكر فيها زي الطابور بتاع الكاشير اللي ييجي الأول يدخل الأول أو يمشي الأول يعني 
# Some important terminology to keep in mind is engueue and dequeue. When we add an item to the queue, we say we engueue the item

# peek()
# seeing the first item in the queue without removing it 

# priority Queue 
# each element has a priority associated with it 