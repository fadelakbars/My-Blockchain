class Block:
    """
        Block adalah wadah untuk menyimpan transaksi  
    """
    
    def __init__(self, Height, Blocksize, BlockHeader, TxCount, Txs):
        self.Height = Height
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.Txcount = TxCount
        self.Txs = Txs