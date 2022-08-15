# The primary task is that node 1 should mine another block and send it to node 2.
# using the generate() function we will generate a block through node 1.
# Now we have to send the mined block to node 2. sync_blocks() function will help us to send it to node 2.
# Now we have to check whether Node 2 recieved the mined block or not. This can be achieved through assert_equal function. To explain in detail, same block was transferred from Node 1 to Node 2 so the hash value for both the blocks in Node 1 and Node 2 should be same as they are the same blocks and not different. So we compare it using assert_equal function to check if it satisfies.

# code starts --> 

def run_test(self):
    self.nodes[1].generate(1)
    self.sync_blocks()

assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())