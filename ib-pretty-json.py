def prettyJSON(A):
    result = []
    indent = 0
    new_line_start = 0

    for i, char in enumerate(A):
        if char == '{' or char == '[':
            if len(A[new_line_start:i]) > 0:
                result.append(indent*'\t' + A[new_line_start:i])
            result.append('\t'*indent + char)
            indent += 1
            new_line_start = i+1
        elif char == ',':
            if len(A[new_line_start:i+1]) == 1:
                result[-1] += ','
            else:
                result.append(indent*'\t' + A[new_line_start:i+1])
            new_line_start = i+1
        elif char == '}' or char == ']':
            if len(A[new_line_start:i]) > 0:
                result.append(indent*'\t' + A[new_line_start:i])
            indent -= 1
            result.append(indent*'\t' + char)
            new_line_start  = i+1
    return result


A = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
# A = '{"id":100,"firstName":"Jack","lastName":"Jones","age":12}'
# A = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
A = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'
for i in prettyJSON(A):
    print(i)