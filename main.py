from unittest import TestCase

import helper
import merkleblock

from block import Block
from helper import (
    bytes_to_bit_field,
    hash256,
    little_endian_to_int,
    read_varint,
)
from merkleblock import (
    MerkleBlock,
    MerkleTree,
)

# 宣言した関数の引数は呼び出されるときに代入されるので一旦放置してOK
# マークルルート:merkle_root関数を実行する際にhashes配列を与える

#親ハッシュを計算する
def merkle_parent(hash1, hash2):
    '''Takes the binary hashes and calculates the hash256'''
    return hash256(hash1 + hash2)

#マークルペアレントレベルに対応する新しいハッシュリストを作成する
def merkle_parent_level(hashes):
    #hashes配列の長さが半分のリストを返す⇔best16右best8になるということ
    if len(hashes) % 2 == 1:
        hashes.append(hashes[-1])
    elif len(hashes) % 2 == 0:
        raise RuntimeError('Cannot take a parent level with only 1 item')

    parent_level = []
    for i in range(1, len(hashes), 2):
      parent = merkle_parent(hashes[i], hashes[i+1])
      parent_level.append(parent)
    return(parent_level)
  
#マークルルートを求める
def merkle_root(hashes):
    current_parent_level = hashes
    while len(current_parent_level) > 1:
        current_parent_level = merkle_parent_level(current_parent_level)
    print(current_parent_level[0])

#トランザクションハッシュをブロックの初期化のパラメータとして設定・エンディアン問題の解決
def validate_merkle_root(self):
    hashes = [h[::-1] for h in self.tx_hashes]
    root = merkle_root(hashes)
    return root[::-1] == self.merkle_root


#関数の実行
merkle_root()