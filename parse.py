tokens = (
    'QUESTION', 'OPTIONS', 'ANSWER',
    'SAY', 'CUTSCENE', 'THINK',
    'MUSIC', 'SFX',
    'STRING', 'NUMBER',
    'RETURN', 'CONTINUE', 'NEXT',
    'COMMA', 'LBRACE', 'RBRACE',
    'EVIDENCE', 'NAME', 'PROFILE',
    'PENALIZE',
    'SLEEP', 'CLS',
    'ADD', 'ADDS',
    'CE', 'PRESS', 'PRESENT',
    'DEFAULT',
    'TESTIMONY', 'STATEMENT',
    'END',
    'OBJECTION', 'HOLDIT', 'TAKETHAT',
    'PROVE',
    'FLAG', 'SET', 'RESET',
    'IF', 'ELSE', 'WHEN',
    'EQUALS',
    'PLACE', 'COLON',
    'MOVE', 'EXAMINE',
    'NOT', 'DESC', 'PERSON', 'TALK', 'CLONE',
    'START', 'ENTER', 'PRINT'
)


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


t_COMMA = ','
t_LBRACE = '{'
t_RBRACE = '}'
t_EQUALS = '='
t_COLON = ':'
t_NOT = '!'


def t_RETURN(t):
    r'(?i)RETURN'
    t.value = 'RETURN'
    return t


def t_CONTINUE(t):
    r'(?i)CONTINUE'
    t.value = 'CONTINUE'
    return t


def t_QUESTION(t):
    r'(?i)QUESTION'
    t.value = 'QUESTION'
    return t


def t_SAY(t):
    r'(?i)SAY'
    t.value = 'SAY'
    return t


def t_OPTIONS(t):
    r'(?i)OPTIONS'
    t.value = 'OPTIONS'
    return t


def t_ANSWER(t):
    r'(?i)ANSWER'
    t.value = 'ANSWER'
    return t


def t_PRINT(t):
    r'(?i)PRINT'
    t.value = 'PRINT'
    return t


def t_MUSIC(t):
    r'(?i)MUSIC'
    t.value = 'MUSIC'
    return t


def t_SFX(t):
    r'(?i)SFX'
    t.value = 'SFX'
    return t


def t_PENALIZE(t):
    r'(?i)PENALIZE'
    t.value = 'PENALIZE'
    return t


def t_SLEEP(t):
    r'(?i)SLEEP'
    t.value = 'SLEEP'
    return t


def t_CUTSCENE(t):
    r'(?i)CUTSCENE'
    t.value = 'CUTSCENE'
    return t


def t_THINK(t):
    r'(?i)THINK'
    t.value = 'THINK'
    return t


def t_CLS(t):
    r'(?i)CLS'
    t.value = 'CLS'
    return t


def t_ADDS(t):
    r'(?i)ADDS'
    t.value = 'ADDS'
    return t


def t_ADD(t):
    r'(?i)ADD'
    t.value = 'ADD'
    return t


def t_PROFILE(t):
    r'(?i)PROFILE'
    t.value = 'PROFILE'
    return t


def t_EVIDENCE(t):
    r'(?i)EVIDENCE'
    t.value = 'EVIDENCE'
    return t


def t_CE(t):
    r'(?i)CROSS-EXAMINATION'
    t.value = 'CROSS-EXAMINATION'
    return t


def t_PRESS(t):
    r'(?i)PRESS'
    t.value = 'PRESS'
    return t


def t_PRESENT(t):
    r'(?i)PRESENT'
    t.value = 'PRESENT'
    return t


def t_DEFAULT(t):
    r'(?i)DEFAULT'
    t.value = 'DEFAULT'
    return t


def t_NEXT(t):
    r'(?i)NEXT'
    t.value = 'NEXT'
    return t


def t_TESTIMONY(t):
    r'(?i)TESTIMONY'
    t.value = 'TESTIMONY'
    return t


def t_STATEMENT(t):
    r'(?i)STATEMENT'
    t.value = 'STATEMENT'
    return t


def t_END(t):
    r'(?i)END'
    t.value = 'END'
    return t


def t_OBJECTION(t):
    r'(?i)OBJECTION'
    t.value = 'OBJECTION'
    return t


def t_HOLDIT(t):
    r'(?i)HOLDIT'
    t.value = 'HOLDIT'
    return t


def t_TAKETHAT(t):
    r'(?i)TAKETHAT'
    t.value = 'TAKETHAT'
    return t


def t_PROVE(t):
    r'(?i)PROVE'
    t.value = 'PROVE'
    return t


def t_FLAG(t):
    r'(?i)FLAG'
    t.value = 'FLAG'
    return t


def t_RESET(t):
    r'(?i)RESET'
    t.value = 'RESET'
    return t


def t_SET(t):
    r'(?i)SET'
    t.value = 'SET'
    return t


def t_IF(t):
    r'(?i)IF'
    t.value = 'IF'
    return t


def t_ELSE(t):
    r'(?i)ELSE'
    t.value = 'ELSE'
    return t


def t_WHEN(t):
    r'(?i)WHEN'
    t.value = 'WHEN'
    return t


def t_PLACE(t):
    r'(?i)PLACE'
    t.value = 'PLACE'
    return t


def t_MOVE(t):
    r'(?i)MOVE'
    t.value = 'MOVE'
    return t


def t_EXAMINE(t):
    r'(?i)EXAMINE'
    t.value = 'EXAMINE'
    return t


def t_DESC(t):
    r'(?i)DESC'
    t.value = 'DESC'
    return t


def t_PERSON(t):
    r'(?i)PERSON'
    t.value = 'PERSON'
    return t


def t_TALK(t):
    r'(?i)TALK'
    t.value = 'TALK'
    return t


def t_CLONE(t):
    r'(?i)CLONE'
    t.value = 'CLONE'
    return t


def t_START(t):
    r'(?i)START'
    t.value = 'START'
    return t

def t_ENTER(t):
    r'(?i)ENTER'
    t.value = 'ENTER'
    return t


def t_STRING(t):
    r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''
    t.value = t.value[1:-1].decode('string_escape')
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]+'
    return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex

lex.lex()


def p_stmtblock(t):
    '''stmtblock : statement stmtblock
                 | statement'''
    if len(t) > 2:
        t[0] = [t[1]] + t[2]
    else:
        t[0] = [t[1]]


def p_statement(t):
    '''statement : say
                 | think
                 | question
                 | music
                 | sfx
                 | return
                 | continue
                 | next
                 | penalize
                 | sleep
                 | cutscene
                 | cls
                 | add
                 | ce
                 | testimony
                 | objection
                 | holdit
                 | takethat
                 | prove
                 | if
                 | ifelse
                 | set
                 | reset
                 | changeplace
                 | place
                 | clone
                 | person
                 | changeperson
                 | start
                 | print'''
    t[0] = t[1]


def p_print(t):
    'print : PRINT STRING'
    t[0] = ['print', t[2]]


def p_say(t):
    'say : SAY STRING COMMA STRING'
    t[0] = ['dialog', t[2], t[4]]


def p_question(t):
    'question : QUESTION STRING OPTIONS stringlist LBRACE answerlist RBRACE'
    t[0] = ['question', t[2], t[4], t[6]]


def p_stringlist(t):
    '''stringlist : STRING COMMA stringlist
                  | STRING'''
    if len(t) > 2:
        t[0] = [t[1]] + t[3]
    else:
        t[0] = [t[1]]


def p_answerlist(t):
    '''answerlist : answer answerlist
                  | answer'''
    if len(t) > 2:
        t[0] = t[1]
        t[0].update(t[2])
    else:
        t[0] = t[1]


def p_answer(t):
    'answer : ANSWER numberlist LBRACE stmtblock RBRACE'
    t[0] = {}
    for i in t[2]:
        t[0].update({i: t[4]})


def p_numberlist(t):
    '''numberlist : NUMBER COMMA numberlist
                  | NUMBER'''
    if len(t) > 2:
        t[0] = [t[1]] + t[3]
    else:
        t[0] = [t[1]]


def p_music(t):
    'music : MUSIC STRING'
    t[0] = ['music', t[2]]


def p_return(t):
    'return : RETURN'
    t[0] = ['return']


def p_continue(t):
    'continue : CONTINUE'
    t[0] = ['continue']


def p_next(t):
    'next : NEXT'
    t[0] = ['next']


def p_sfx(t):
    'sfx : SFX STRING'
    t[0] = ['sfx', t[2]]


def p_penalize(t):
    'penalize : PENALIZE'
    t[0] = ['penalize']


def p_sleep(t):
    'sleep : SLEEP NUMBER'
    t[0] = ['sleep', t[2]]


def p_cutscene(t):
    'cutscene : CUTSCENE STRING'
    t[0] = ['cutscene', t[2]]


def p_think(t):
    'think : THINK STRING COMMA STRING'
    t[0] = ['think', t[2], t[4]]


def p_cls(t):
    'cls : CLS'
    t[0] = ['cls']


def p_add(t):
    'add : addt type STRING COMMA STRING COMMA NAME'
    t[0] = ['add', t[2], t[3], t[5], t[1], t[7]]


def p_addt(t):
    '''addt : ADD
            | ADDS'''
    t[0] = (True if t[1] == 'ADDS' else False)


def p_type(t):
    '''type : PROFILE
            | EVIDENCE'''
    t[0] = t[1]


def p_ce(t):
    'ce : CE LBRACE plist RBRACE'
    t[0] = ['cross-examination', t[3]]


def p_plist(t):
    '''plist : PRESS numberlist LBRACE stmtblock RBRACE plist
             | PRESENT NAME COMMA numberlist LBRACE stmtblock RBRACE plist
             | PRESENT DEFAULT LBRACE stmtblock RBRACE plist
             | when plist
             | END LBRACE stmtblock RBRACE plist
             |'''
    if len(t) > 1:
        if t[1] == 'PRESS':
            t[0] = t[6]
            for i in t[2]:
                t[0]['press'][i] = t[4]
        elif t[1] == 'PRESENT':
            if t[2] == 'DEFAULT':
                t[0] = t[6]
                t[0]['present']['default'] = t[4]
            else:
                t[0] = t[8]
                for i in t[4]:
                    if i not in t[0]['present']:
                        t[0]['present'][i] = {}
                    t[0]['present'][i][t[2]] = t[6]
        elif isinstance(t[1], list):
            t[0] = t[2]
            t[0]['when'].append(t[1][1:])
        else:
            t[0] = t[5]
            t[0]['end'] = t[3]
    else:
        t[0] = {'press': {}, 'present': {}, 'when': []}


def p_testimony(t):
    'testimony : TESTIMONY STRING COMMA STRING LBRACE statementlist RBRACE'
    t[0] = ['testimony', t[2], t[4], t[6]]


def p_statementlist(t):
    '''statementlist : STATEMENT STRING statementlist
                     | STATEMENT STRING'''
    if len(t) > 3:
        t[0] = [t[2]] + t[3]
    else:
        t[0] = [t[2]]


def p_objection(t):
    'objection : OBJECTION STRING'
    t[0] = ['objection', t[2]]


def p_holdit(t):
    'holdit : HOLDIT STRING'
    t[0] = ['holdit', t[2]]


def p_takethat(t):
    'takethat : TAKETHAT STRING'
    t[0] = ['takethat', t[2]]


def p_prove(t):
    'prove : PROVE STRING LBRACE provelist RBRACE'
    t[0] = ['prove', t[2], t[4]]


def p_provelist(t):
    '''provelist : PRESENT DEFAULT LBRACE stmtblock RBRACE provelist
                 | PRESENT NAME LBRACE stmtblock RBRACE provelist
                 | '''
    if len(t) > 1:
        t[0] = t[6]
        if t[2] == 'DEFAULT':
            t[0]['default'] = t[4]
        else:
            t[0][t[2]] = t[4]
    else:
        t[0] = {}


def p_if(t):
    'if : IF conditions LBRACE stmtblock RBRACE'
    t[0] = ['if', t[2], t[4]]


def p_ifelse(t):
    'ifelse : IF conditions LBRACE stmtblock RBRACE ELSE LBRACE stmtblock RBRACE'
    t[0] = ['ifelse', t[2], t[4], t[8]]


# def p_namelist(t):
#     '''namelist : NAME COMMA namelist
#                 | NAME'''
#     if len(t) == 2:
#         t[0] = [t[1]]
#     else:
#         t[0] = [t[1]] + t[3]

def p_conditions(t):
    '''conditions : NAME COMMA conditions
                  | NOT NAME COMMA conditions
                  | PLACE EQUALS NAME COMMA conditions
                  | NAME
                  | NOT NAME
                  | PLACE EQUALS NAME'''
    if len(t) == 2:
        t[0] = [['name', t[1]]]
    elif len(t) == 4 and t[1] == 'PLACE':
        t[0] = [['place', t[3]]]
    elif len(t) == 3:
        t[0] = [['not', t[2]]]
    elif t[1] == '!':
        t[0] = [['not', t[2]]] + t[4]
    elif t[2] == ',':
        t[0] = [['name', t[1]]] + t[3]
    else:
        t[0] = [['place', t[3]]] + t[5]


def p_set(t):
    'set : SET FLAG NAME'
    t[0] = ['set', t[3]]


def p_reset(t):
    'reset : RESET FLAG NAME'
    t[0] = ['reset', t[3]]


def p_when(t):
    'when : WHEN conditions LBRACE stmtblock RBRACE'
    t[0] = ['when', t[2], t[4]]


def p_changeplace(t):
    'changeplace : NAME COLON placeattr'
    t[0] = ['changeplace', t[1], t[3]]


def p_changeperson(t):
    'changeperson : NAME COLON personattr'
    t[0] = ['changeperson', t[1], t[3]]


def p_start(t):
    'start : START NAME'
    t[0] = ['start', t[2]]


def p_placeattr(t):
    '''placeattr : MOVE NAME
                 | EXAMINE stringlist LBRACE stmtblock RBRACE
                 | EXAMINE DEFAULT LBRACE stmtblock RBRACE
                 | ENTER LBRACE stmtblock RBRACE
                 | DESC STRING
                 | PERSON NAME
                 | MUSIC STRING'''
    if t[1] == 'MOVE':
        t[0] = ['move', t[2]]
    elif t[2] == 'DEFAULT':
        t[0] = ['examine', ['default'], t[4]]
    elif t[1] == 'ENTER':
        t[0] = ['enter', t[3]]
    elif t[1] == 'EXAMINE':
        t[0] = ['examine', t[2], t[4]]
    elif t[1] == 'MUSIC':
        t[0] = ['music', t[2]]
    elif t[1] == 'PERSON':
        if t[2] == 'none':
            t[0] = ['person', None]
        else:
            t[0] = ['person', t[2]]
    else:
        t[0] = ['desc', t[2]]


def p_plattrlist(t):
    '''plattrlist : placeattr plattrlist
                 | when plattrlist
                 | '''
    if len(t) == 1:
        t[0] = {'move': [], 'examine': {}, 'desc': '', 'when': [], 'person': None, 'enter': [], 'music': 'stop'}
    else:
        attr = t[1]
        d = t[2]
        if attr[0] == 'move':
            d['move'].append(attr[1])
        elif attr[0] == 'examine':
            for i in attr[1]:
                d['examine'][i] = attr[2]
        elif attr[0] == 'desc':
            d['desc'] = attr[1]
        elif attr[0] == 'person':
            d['person'] = attr[1]
        elif attr[0] == 'enter':
            d['enter'] = attr[1]
        elif attr[0] == 'music':
            d['music'] = attr[1]
        else:
            d['when'].append(attr[1:])
        t[0] = d


def p_personattr(t):
    '''personattr : TALK NUMBER LBRACE stmtblock RBRACE
                  | PRESENT NAME LBRACE stmtblock RBRACE
                  | PRESENT DEFAULT LBRACE stmtblock RBRACE'''
    if t[1] == 'TALK':
        t[0] = ['talk', t[2], t[4]]
    elif t[2] == 'DEFAULT':
        t[0] = ['present', 'default', t[4]]
    elif t[1] == 'PRESENT':
        t[0] = ['present', t[2], t[4]]


def p_psattrlist(t):
    '''psattrlist : personattr psattrlist
                  | '''
    if len(t) == 1:
        t[0] = {'present': {}, 'talk': {}}
    else:
        attr = t[1]
        d = t[2]
        if attr[0] == 'talk':
            d['talk'][attr[1]] = attr[2]
        else:
            d['present'][attr[1]] = attr[2]
        t[0] = d


def p_place(t):
    'place : PLACE NAME COMMA STRING LBRACE plattrlist RBRACE'
    t[0] = ['place', t[2], t[4], t[6]]


def p_clone(t):
    'clone : CLONE NAME COMMA NAME'
    t[0] = ['clone', t[2], t[4]]


def p_person(t):
    'person : PERSON NAME COMMA STRING COMMA stringlist LBRACE psattrlist RBRACE'
    t[0] = ['person', t[2], t[4], t[6], t[8]]


def p_error(t):
    print("Syntax error at token '%s' (%s) [Line %i]" % (t.value, t.type, t.lineno))


import ply.yacc as yacc

yacc.yacc()


def parse(string):
    return yacc.parse(string)
