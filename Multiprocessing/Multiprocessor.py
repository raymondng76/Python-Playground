import time
import concurrent.futures


# For CPU heavy task, use concurrent.futures.ProcessPoolExecutor
# For I/O heavy task (Reading/writing from/to disk, downloading from internet) use concurrent.futures.ThreadPoolExecutor

def action(seconds): # Sample method to simulate delay
    print(f'Action performed for {seconds} second(s).')
    time.sleep(seconds)
    return f'Action for {seconds} second(s) done.'

if __name__ == '__main__':
    st = time.perf_counter()  

    # Using submit method
    # with concurrent.futures.ProcessPoolExecutor() as exe: # This is the multiprocessor used with context manager 
    #     r1 = exe.submit(action, 1) # The submit method submit the method and their arguments
    #     r2 = exe.submit(action, 2) # For additional method call, repeat the submit method call
    #     r3 = exe.submit(action, 3)
    #     r4 = exe.submit(action, 4)
    #     r5 = exe.submit(action, 5)

    #     print(r1.result()) # .result() gets the return object from the action method passed into submit method
    #     print(r2.result()) # The results return is in the order of completion
    #     print(r3.result())
    #     print(r4.result())
    #     print(r5.result())

        ##############################
        # Action performed for 1 seconds(s).
        # Action performed for 2 seconds(s).
        # Action performed for 3 seconds(s).
        # Action performed for 4 seconds(s).
        # Action performed for 5 seconds(s).
        # Action for 1 second(s) done.
        # Action for 2 second(s) done.
        # Action for 3 second(s) done.
        # Action for 4 second(s) done.
        # Action for 5 second(s) done.
        ##############################



    # Using submit method with list comprehension
    # with concurrent.futures.ProcessPoolExecutor() as exe:
    #     secs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #     results = [exe.submit(action, sec) for sec in secs] # list comprehension to loop thru the submit method multiple time with list of options

    #     for f in concurrent.futures.as_completed(results): # use as_completed to get a collate set of return results
    #         print(f.result()) # The results return is in the order of completion

        ##############################
        # Action performed for 10 seconds(s).
        # Action performed for 9 seconds(s).
        # Action performed for 8 seconds(s).
        # Action performed for 7 seconds(s).
        # Action performed for 6 seconds(s).
        # Action performed for 5 seconds(s).
        # Action performed for 4 seconds(s).
        # Action performed for 3 seconds(s).
        # Action performed for 2 seconds(s).
        # Action performed for 1 seconds(s).
        # Action for 1 second(s) done.
        # Action for 2 second(s) done.
        # Action for 3 second(s) done.
        # Action for 4 second(s) done.
        # Action for 5 second(s) done.
        # Action for 6 second(s) done.
        # Action for 7 second(s) done.
        # Action for 8 second(s) done.
        # Action for 9 second(s) done.
        # Action for 10 second(s) done.
        ##############################



    # Using map function
    with concurrent.futures.ProcessPoolExecutor() as exe:
        secs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        results = exe.map(action, secs) # Use map method to process action method for each element in secs

        for r in results: # Get the output directly
            print(r) # The results return is in the order of their execution
        
        ##############################
        # Action performed for 10 seconds(s).
        # Action performed for 9 seconds(s).
        # Action performed for 8 seconds(s).
        # Action performed for 7 seconds(s).
        # Action performed for 6 seconds(s).
        # Action performed for 5 seconds(s).
        # Action performed for 4 seconds(s).
        # Action performed for 3 seconds(s).
        # Action performed for 2 seconds(s).
        # Action performed for 1 seconds(s).
        # Action for 10 second(s) done.
        # Action for 9 second(s) done.
        # Action for 8 second(s) done.
        # Action for 7 second(s) done.
        # Action for 6 second(s) done.
        # Action for 5 second(s) done.
        # Action for 4 second(s) done.
        # Action for 3 second(s) done.
        # Action for 2 second(s) done.
        # Action for 1 second(s) done.
        ##############################

    ft = time.perf_counter()
    print(f'Total time {round(ft-st, 2)} seconds(s).')