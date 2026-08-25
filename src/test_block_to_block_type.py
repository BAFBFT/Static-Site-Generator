import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlocktoBlockType(unittest.TestCase):
    def test_unordered_list(self):
        block =  "- This is a list\n- with items"
        self.assertEqual(block_to_block_type(block), 
                         BlockType.UNORDERED_LIST)
        
if __name__ == "__main__":
    unittest.main()