from datetime import datetime as _dt
from hashlib import sha256 as _s256
from json import dumps as _dumps

class Chain:
    
    def __init__(self) -> None:
        self.chain = [self.create_block(data="genesis", proof=1, prev_hash="0", index=1)]
        self.hardness = 4

    def mine_block(self,data:str)-> dict:
        prev_block = self.get_prev_block()
        index = prev_block["index"] + 1
        proof = self.proof_of_work(prev_proof=prev_block["proof"], index=index, data=data)
        prev_hash = self._hash(block=prev_block)
        block = self.create_block(data=data, proof=proof, prev_hash=prev_hash, index=index)
        self.chain.append(block)
        return block

    def _hash(self, block:dict)-> str:
        encoded_block = _dumps(block, sort_keys=True).encode()
        return _s256(encoded_block).hexdigest()

    def to_digest(self, new_proof: int, prev_proof : int, index: int, data: str) -> bytes:
       return str(str(new_proof ** 2 + prev_proof ** 2 + index) + data).encode()
    

    def proof_of_work(self, prev_proof : int, index : int, data : str) -> int:
        new_proof = 1
        hardness = "0" * self.hardness 
        while not _s256(self.to_digest(new_proof, prev_proof, index, data)).hexdigest().startswith(hardness):
            new_proof += 1
        return new_proof


    def get_prev_block(self) -> dict:
        return self.chain[-1]
    

    def create_block(self, data : str, proof : int, prev_hash: str, index : int) -> dict:
        return {
            "index" : index,
            "timestamp" : int(_dt.now().timestamp() * 1000000),
            "data" : data,
            "proof" : proof,
            "prev_hash" : prev_hash
        }