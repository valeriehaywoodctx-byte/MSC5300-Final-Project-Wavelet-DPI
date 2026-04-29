graph TD
    Root[Root Node: Level 0] --> L1[Left Child: Bit=0]
    Root --> R1[Right Child: Bit=1]
    L1 --> L2[Sub-tree: Range 0-63]
    L1 --> R2[Sub-tree: Range 64-127]
    R1 --> L3[Sub-tree: Range 128-191]
    R1 --> R3[Sub-tree: Range 192-255]