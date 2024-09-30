from typing import List, Optional

def match(pattern: List[str], source: List[str]) -> Optional[List[str]]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """
    sind = 0                
    pind = 0                
    result: List[str] = []  # sub

    while pind < len(pattern):
        # multi word wildcard
        if pattern[pind] == '%':
            # end term wildcard
            if pind == len(pattern) - 1:
                matched = ' '.join(source[sind:]) if sind < len(source) else ''
                result.append(matched)
                sind = len(source)
                pind += 1
            else:
                # get forward case
                next_pattern = pattern[pind + 1]
                next_pos = sind
                matched = []
                found = False
                while next_pos <= len(source):
                    if next_pos < len(source) and source[next_pos] == next_pattern:
                        found = True
                        break
                    matched.append(source[next_pos] if next_pos < len(source) else '')
                    next_pos += 1
                if found:
                    matched_str = ' '.join(source[sind:next_pos])
                    result.append(matched_str)
                    sind = next_pos
                    pind += 1
                else:
                    # no match
                    return None
        elif pattern[pind] == '_':
            if sind >= len(source):
                return None  # nothing
            result.append(source[sind])
            sind += 1
            pind += 1
        else:
            if sind >= len(source) or pattern[pind] != source[sind]:
                return None 
            sind += 1
            pind += 1

    if sind == len(source):
        return result
    else:
        return None

if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
    # this last case is a strange one, but it exposes an issue with the way we've
    # written our match function
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
