def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1
 
    if left >= len(heap):
        return idx
    
    if right < len(heap) and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[idx] < heap[index_largest]:
        tmp = heap[idx]
        heap[idx] = heap[index_largest]
        heap[index_largest] = tmp
        return sift_down(heap, index_largest) 
    else:
        return idx

   
def test():
    sample = [0, 0, 9, 6, 2, 4, 1]
    assert sift_down(sample, 1) == 5
