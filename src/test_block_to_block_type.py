import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlocktoBlockType(unittest.TestCase):
    def test_unordered_list(self):
        block =  "- This is a list\n- with items"
        self.assertEqual(block_to_block_type(block), 
                         BlockType.UNORDERED_LIST)
    
    def test_mixed_list(self):
        block =  "- This is a list\n- with items\n1. And some ordered\n2.Items"
        self.assertEqual(block_to_block_type(block), 
                         BlockType.PARAGRAPH)
    
    
    def test_invalid_ordered_list(self):
        block =  "1. This is an invalid \n2. ordered list\n4. should not be classifed as one"
        self.assertNotEqual(block_to_block_type(block), 
                         BlockType.ORDERED_LIST)
        
if __name__ == "__main__":
    unittest.main()