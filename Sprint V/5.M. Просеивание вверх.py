def sift_up(heap, idx):
    if idx == 1:
        return idx

    parent_idx = idx // 2

    if heap[parent_idx] < heap[idx]:
        tmp = heap[parent_idx]
        heap[parent_idx] = heap[idx]
        heap[idx] = tmp
        return sift_up(heap, parent_idx)
    else:
        return idx
  
  
def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


test()
