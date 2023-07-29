from linked_list import LinkedList


def loop_detection(l1):
    #intialize the fast pointer to the head of the LL
    fast = l1.head
    #initialize the slow pointer to the head of LL
    slow = l1.head

    #Move the fast pointer two steps ahead and the slow pointer one step ahead until they meet
    while fast and fast.next:
        #Fast pointer moves the two steps at a time
        fast = fast.next.next
        #Slow pointer moves one step at a time
        slow = slow.next 
        #If the fast and slow pointer meet a loop is detected.
        if fast is slow:
            break
    
    #If the fast pointer reaches the end of the LL, no loop is present
    if fast is None or fast.next is None:
        return None

    #Reset the slow pointer to the head of the LL
    slow = l1.head

    #Move both the fast and slow pointer one step at a time until they meet at the beggining of the loop
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    #return the node at the beginning of the loop
    return fast


'''
Unit test for the loop detection algorithm.
It sets up different test scenarios by creating various linked lists

The test cases are defined as tuples, where the first element is a linked list and the second element is the expected start node.


'''
def test_loop_detection():
    looped_list = LinkedList(["A", "8", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next.next
    looped_list.tail.next = loop_start_node

    tests = [
        #Test case with an empty linked list
        (LinkedList(), None),
        #Test case with a non-looped linked list
        ((LinkedList((1, 2, 3))), None),
        #Test case with a looped linked list
        (looped_list, loop_start_node),
    ]

    #Iterate over the test cases
    for l1, expected in tests:
        #Verify that the loop detection function returns the expected loop start node
        assert loop_detection(l1) == expected
        
        # Check the overall result of the tests
    if len(tests) == 0:
        print("No tests found.")
    elif len(tests) == 1:
        print("Only one test found.")
    elif len(tests) > 1:
        try:
            assert all(loop_detection(l1) == expected for l1, expected in tests)
            print("All tests passed!")
        except AssertionError:
            failed_tests = [i + 1 for i, (l1, expected) in enumerate(tests) if loop_detection(l1) != expected]
            if failed_tests:
                print(f"Some tests failed: {failed_tests}")
            else:
                print("All tests failed!")
test_loop_detection()