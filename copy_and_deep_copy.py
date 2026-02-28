from copy import copy, deepcopy

"""
Python Copy vs Deep Copy Demonstration
=======================================
This module demonstrates the difference between assignment, shallow copy,
and deep copy in Python using list examples.

Key Concepts:
- Assignment (=)   : Both variables point to the SAME object in memory.
- Shallow Copy     : Creates a new object, but nested objects are still shared.
- Deep Copy        : Creates a fully independent clone — including all nested objects.
"""

# ─────────────────────────────────────────────
# SECTION 1: Assignment (=)
# Both l1 and l2 point to the exact same list object.
# Any change to l1 is reflected in l2 (they are the same object).
# ─────────────────────────────────────────────
l1 = [1, 2, 3]
l2 = l1          # l2 is NOT a copy — it's just another name for the same list
l1[0] = 0        # modifying l1 also modifies l2

print(l1)        # [0, 2, 3]
print(l2)        # [0, 2, 3]  ← changed because l1 and l2 are the same object
print(id(l1))    # same memory address
print(id(l2))    # same memory address ↑


# ─────────────────────────────────────────────
# SECTION 2: Shallow Copy — flat list
# copy() creates a NEW list object, but with references to the same elements.
# For flat lists (no nested objects), this behaves like a true independent copy.
# ─────────────────────────────────────────────
l1 = [1, 2, 3]
l2 = copy(l1)    # l2 is a new list with the same values
l1[0] = 0        # modifying l1 does NOT affect l2 (integers are immutable)

print(l1)        # [0, 2, 3]
print(l2)        # [1, 2, 3]  ← unaffected, since integers are immutable
print(id(l1))    # different memory address
print(id(l2))    # different memory address ↑


# ─────────────────────────────────────────────
# SECTION 3: Shallow Copy — nested list (limitation exposed)
# copy() only copies the top-level structure.
# Nested objects (like inner lists) are still SHARED between l1 and l2.
# Mutating a nested object through l1 WILL affect l2.
# ─────────────────────────────────────────────
l1 = [1, 2, 3, [1, 2, 3]]
l2 = copy(l1)    # shallow copy: new outer list, but inner list is shared

l1[0] = 0        # top-level change — does NOT affect l2 (immutable int replaced)
l1[3][0] = 0     # nested change — DOES affect l2 (same inner list object)

print(l1)        # [0, 2, 3, [0, 2, 3]]
print(l2)        # [1, 2, 3, [0, 2, 3]]  ← inner list was mutated!
print(id(l1))    # different address (outer list is a new object)
print(id(l2))    # different address ↑, but id(l1[3]) == id(l2[3])


# ─────────────────────────────────────────────
# SECTION 4: Deep Copy — nested list (fully independent)
# deepcopy() recursively copies all objects, including nested structures.
# l1 and l2 are completely independent — no shared references at any level.
# ─────────────────────────────────────────────
l1 = [1, 2, 3, [1, 2, 3]]
l2 = deepcopy(l1)   # full independent clone, including nested list

l1[0] = 0           # top-level change — does NOT affect l2
l1[3][0] = 0        # nested change — does NOT affect l2 (separate inner list)

print(l1)           # [0, 2, 3, [0, 2, 3]]
print(l2)           # [1, 2, 3, [1, 2, 3]]  ← fully unaffected
print(id(l1))       # different address
print(id(l2))       # different address, and id(l1[3]) != id(l2[3]) too