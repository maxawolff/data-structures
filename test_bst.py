"""Test for bst."""
import pytest
import pdb


@pytest.fixture
def new_bst():
    """."""
    from bst import BST
    b = BST()
    b.insert(20)
    return b


@pytest.fixture
def bst_d1():
    """."""
    from bst import BST
    b = BST()
    b.insert(20)
    b.insert(10)
    b.insert(30)
    return b


@pytest.fixture
def big_bst():
    """."""
    from bst import BST
    b = BST()
    b.insert(20)
    b.insert(10)
    b.insert(30)
    b.insert(5)
    b.insert(15)
    b.insert(25)
    b.insert(40)
    b.insert(3)
    b.insert(27)
    b.insert(33)
    b.insert(42)
    b.insert(4)
    return b


def test_node_has_val():
    """."""
    from bst import Node
    n = Node(4)
    assert n.value == 4


def test_bst_add_one_node_becomes_head():
    """Adding one node should make it the head."""
    from bst import BST
    b = BST()
    b.insert(4)
    assert b.head.value == 4


def test_bst_add_two_nodes_second_smaller(new_bst):
    """Adding a node smaller than the head should set left."""
    new_bst.insert(8)
    assert new_bst.head.left.value == 8


def test_bst_add_two_nodes_second_largeer(new_bst):
    """Adding a node larger than the head should set left."""
    new_bst.insert(30)
    assert new_bst.head.right.value == 30


def test_bst_depth_of_1(bst_d1):
    """BST with left and right value."""
    assert bst_d1.head.right.value == 30
    assert bst_d1.head.left.value == 10


def test_bst_d1_add_left_left(bst_d1):
    """Add a value to the left of the left of head."""
    bst_d1.insert(5)
    assert bst_d1.head.left.left.value == 5


def test_bst_d1_add_left_left_left(bst_d1):
    """Add a value to the left of the left of head."""
    bst_d1.insert(5)
    bst_d1.insert(2)
    assert bst_d1.head.left.left.left.value == 2


def test_bst_d1_add_left_left_left_and_right(bst_d1):
    """Add a value to the left of the left of head."""
    bst_d1.insert(5)
    bst_d1.insert(2)
    bst_d1.insert(4)
    assert bst_d1.head.left.left.left.value == 2
    assert bst_d1.head.left.left.left.right.value == 4


def test_empty_bst_depth_0():
    """An empty bst should have depth 0."""
    from bst import BST
    b = BST()
    assert b.depth() == 0


def test_bst_depth_of_one(new_bst):
    """Bst with one node should have depth of 1."""
    assert new_bst.depth() == 1
    assert new_bst.head.depth == 1


def test_bst_depth_two_nodes_is_2(new_bst):
    """Bst with one node should have depth of 1."""
    new_bst.insert(1)
    assert new_bst.depth() == 2
    assert new_bst.head.left.depth == 2


def test_bst_depth_three_nodes_is_2_when_balanced(new_bst):
    """Bst with one node should have depth of 1."""
    new_bst.insert(1)
    new_bst.insert(30)
    assert new_bst.depth() == 2
    assert new_bst.head.right.depth == 2


def test_bst_depth_three_nodes_is_3_when_unbalanced(new_bst):
    """Bst with one node should have depth of 1."""
    new_bst.insert(1)
    new_bst.insert(5)
    assert new_bst.depth() == 3
    assert new_bst.head.left.right.depth == 3


def test_search_one_node(new_bst):
    """Search for the one node in a bst."""
    assert new_bst.search(20).value == 20


def test_search_one_node_wrong_value_returns_none(new_bst):
    """Search for a node not in a bst."""
    assert new_bst.search(21) is None


def test_search_several_nodes(bst_d1):
    """Search one of the nodes in a bst."""
    assert bst_d1.search(30).value == 30
    assert bst_d1.search(20).value == 20


def test_search_several_nodes_wrong_node(bst_d1):
    """Searching for a node not present returns none."""
    assert bst_d1.search(100000) is None


def test_contains_one_node(new_bst):
    """Search for the one node in a bst."""
    assert new_bst.contains(20) is True


def test_contains_one_node_wrong_value_returns_none(new_bst):
    """Search for a node not in a bst."""
    assert new_bst.contains(21) is False


def test_contains_several_nodes(bst_d1):
    """Search one of the nodes in a bst."""
    assert bst_d1.contains(30) is True
    assert bst_d1.contains(20) is True


def test_contains_several_nodes_wrong_node(bst_d1):
    """Searching for a node not present returns none."""
    assert bst_d1.contains(100000) is False


def test_balance_no_nodes():
    """Balance of empty tree should be 0."""
    from bst import BST
    b = BST()
    assert b.balance() == 0


def test_balance_one_node(new_bst):
    """A bst with one node should be balanced."""
    assert new_bst.balance() == 0


def test_balance_balanced_bst(bst_d1):
    """Should be 0 since balanced."""
    print(bst_d1.left_depth)
    print(bst_d1.right_depth)
    assert bst_d1.balance() == 0


def test_balance_unbalanced_left(new_bst):
    """Should have -1 balanced since depth higher in left."""
    new_bst.insert(10)
    assert new_bst.balance() == -1


def test_balance_unbalanced_right(new_bst):
    """Should have -1 balanced since depth higher in left."""
    new_bst.insert(30)
    assert new_bst.balance() == 1


def test_balance_unbalanced_right_by_two(new_bst):
    """Should have -1 balanced since depth higher in left."""
    new_bst.insert(30)
    new_bst.insert(35)
    assert new_bst.balance() == 2


def test_balance_unbalanced_right_by_three(new_bst):
    """Should have -1 balanced since depth higher in left."""
    new_bst.insert(30)
    new_bst.insert(35)
    new_bst.insert(32)
    assert new_bst.balance() == 3
    assert new_bst.right_depth == 4


def test_balance_unbalanced_right_by_two_four_nodes(new_bst):
    """Should have -1 balanced since depth higher in left."""
    new_bst.insert(30)
    new_bst.insert(35)
    new_bst.insert(25)
    assert new_bst.balance() == 2
    assert new_bst.right_depth == 3


def test_breadth_first_empty_bst():
    """Empty bst should return empty list on traversal."""
    from bst import BST
    b = BST()
    assert b.breadth_first() == []


def test_breadth_first_small_bst(bst_d1):
    """Breadth first should return generator with values in bf order."""
    gen = bst_d1.breadth_first()
    a = next(gen)
    b = next(gen)
    c = next(gen)
    assert a == 20 and b == 10 and c == 30


def test_breadth_first_large_bst(big_bst):
    """Breadth first should return generator with values in bf order."""
    gen = big_bst.breadth_first()
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    expected_output = [20, 10, 30, 5, 15, 25, 40, 3, 27, 33, 42, 4]
    assert values == expected_output


def test_pre_order_large_bst(big_bst):
    """Pre order should return generator with values in pre order."""
    gen = big_bst.pre_order()
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    expected_output = [20, 10, 5, 3, 4, 15, 30, 25, 27, 40, 33, 42]
    assert values == expected_output


def test_in_order_large_bst(big_bst):
    """In order should return generator with values in order."""
    gen = big_bst.in_order()
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    expected_output = [3, 4, 5, 10, 15, 20, 25, 27, 30, 33, 40, 42]
    assert values == expected_output


def test_post_order_large_bst(big_bst):
    """Post order should return generator with values in post order."""
    gen = big_bst.post_order()
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    expected_output = [4, 3, 5, 15, 10, 27, 25, 33, 42, 40, 30, 20]
    assert values == expected_output


def test_delete_value_not_found_raises_error(bst_d1):
    """Trying to delete a value not in bst should raise error."""
    with pytest.raises(ValueError):
        bst_d1.delete(100)


def test_parent_pointer_is_correct(big_bst):
    """Check if new parent pointer points to correct parent node."""
    node1 = big_bst.search(5)
    node2 = big_bst.search(10)
    node3 = big_bst.search(42)
    node4 = big_bst.search(4)
    assert node1.parent.value == 10
    assert node2.parent.value == 20
    assert node3.parent.value == 40
    assert node4.parent.value == 3


def test_delete_node_has_no_kids(bst_d1):
    """Delete a node that has no children."""
    bst_d1.delete(10)
    assert bst_d1.head.left is None
    bst_d1.delete(30)
    assert bst_d1.head.right is None


def test_fld(big_bst):
    """Fld should return the furthest left descendant."""
    node = big_bst.search(10)
    assert big_bst._fld(node).value == 3
    node2 = big_bst.search(30)
    assert big_bst._fld(node2).value == 25


def test_delete_node_has_left_child_only(big_bst):
    """Delete a node that only has a left child."""
    big_bst.delete(10)
    assert big_bst.head.left.value == 15
    assert big_bst.head.left.left.value == 5


def test_delete_head(big_bst):
    """Deleting the head shouldn't mess things up."""
    big_bst.delete(20)
    assert big_bst.head.value == 30
    old_left = big_bst.search(10)
    assert old_left.parent == big_bst.search(25)


def test_delete_node_has_right_child_only(big_bst):
    """Delete a node that only has a left child."""
    big_bst.delete(25)
    node = big_bst.search(27)
    assert node.parent.value == 30


def test_delete_node_has_both_children(big_bst):
    """Delete a node that has two children."""
    big_bst.delete(30)
    assert big_bst.head.right.value == 40
    node = big_bst.search(25)
    assert node.parent.value == 33


def test_delete_node_has_both_children_again(big_bst):
    """Delete a node that has two children."""
    big_bst.delete(10)
    assert big_bst.head.left.value == 15
    node = big_bst.search(5)
    assert node.parent.value == 15


# def test_balance_factor_after_insert(new_bst):
#     """Test method for adjusting balance factor."""
#     assert new_bst.head.balance_factor == 0
#     new_bst.insert(10)
#     assert new_bst.head.balance_factor == -1
#     assert new_bst.head.left.balance_factor == 0


# def test_balance_factor_after_insert2(new_bst):
#     """Test method for adjusting balance factor."""
#     new_bst.insert(10)
#     new_bst.insert(30)
#     assert new_bst.head.balance_factor == 0
#     assert new_bst.head.right.balance_factor == 0


# def test_balance_factor_off_by_2(new_bst):
#     """Test that balance gets properly changed."""
#     new_bst.insert(10)
#     new_bst.insert(5)
#     assert new_bst.head.balance_factor == -2


# def test_autobalance_left_rotation(bst_d1):
#     """Check if a left rotation happens correctly."""
#     bst_d1.insert(5)
#     bst_d1.insert(3)


# def test_fix_everything(bst_d1):
#     """."""
#     bst_d1.insert(5)
#     bst_d1.insert(15)
#     bst_d1.insert(25)
#     bst_d1.insert(40)
#     bst_d1.insert(3)
#     bst_d1.insert(27)
#     bst_d1.insert(33)
#     for node in bst_d1.nodes:
#         pdb.set_trace()
#         print(node.value)
#         print(node.balance_factor)
#     pdb.set_trace()


# def test_balance_as_property():
#     """."""
#     from bst import Node
#     n = Node(10)
#     n.lsd = 3
#     n.rsd = 2
#     assert n.balance == -1


# def test_subdepth_works(new_bst):
#     """Test subdepth updates properly."""
#     assert new_bst.head.lsd == 1
#     assert new_bst.head.rsd == 1


# def test_subdepth_works2(new_bst):
#     """Test subdepth updates properly."""
#     new_bst.insert(10)
#     assert new_bst.head.lsd == 2
#     assert new_bst.head.rsd == 1
#     assert new_bst.head.balance == -1
#     assert new_bst.head.left.lsd == 1
#     assert new_bst.head.left.rsd == 1


# def test_subdepth_works3(new_bst):
#     """Test subdepth updates properly."""
#     new_bst.insert(10)
#     new_bst.insert(30)
#     assert new_bst.head.lsd == 2
#     assert new_bst.head.rsd == 2
#     assert new_bst.head.balance == 0


# def test_subdepth_works4(bst_d1):
    """Test subdepth updates properly."""
    # bst_d1.insert(5)
    # assert bst_d1.head.lsd == 3
    # bst_d1.insert(15)
    # assert bst_d1.head.lsd == 3
    # bst_d1.insert(25)
    # assert bst_d1.head.rsd == 3
    # bst_d1.insert(40)
    # assert bst_d1.head.rsd == 3
    # bst_d1.insert(3)
    # assert bst_d1.head.lsd == 4
    # bst_d1.insert(27)
    # assert bst_d1.head.rsd == 4
    # assert bst_d1.head.left.lsd == 3 and bst_d1.head.left.rsd == 2
    # bst_d1.insert(33)
    # assert bst_d1.head.rsd == 4
