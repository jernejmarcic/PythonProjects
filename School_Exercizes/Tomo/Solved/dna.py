import random
# =============================================================================
# DNA
#
# _Deoxyribonucleic acid_ (_DNA_) is a molecule composed of two chains that coil around each other to form a double helix carrying the genetic instructions used in the growth, development, functioning,
# and reproduction of all known living organisms and many viruses. It is composed of simpler monomeric units called nucleotides. DNA can contain four different nucleotides - _adenine_ (A), _cytosine_ (C),
# _guanine_ (G) and _thymine_ (T).
#
# DNA can be represented as a string or sequence of characters, e.g. `'ACCGCTTAGTACCAGTAG'`.
# =====================================================================@020071=
# 1. podnaloga
# Write a function`get_length(dna)`, which returns the length of DNA sequence `dna`, that is the number of nucleotides in given DNAsequence.
#
# Examples:
#
#     >>> get_length('ATCGAT')
#     6
#     >>> get_length('ATCG')
#     4
# =============================================================================
def get_length(dna):
    return len(dna)

# =====================================================================@020072=
# 2. podnaloga
# Write a function `is_longer(dna1, dna2)`, which returns `True`, if the DNA sequence `dna1` is longer than the DNA sequence `dna2`. Otherwise it returns `False`.
#
# Examples:
#
#     >>> is_longer('ATCG', 'AT')
#     True
#     >>> is_longer('ATCG', 'ATCGGA')
#     False
# =============================================================================

def is_longer(dna1, dna2):
    if len(dna1) > len(dna2):
        return True

    else:
        return False


# =====================================================================@020073=
# 3. podnaloga
# Write a function `nucleotides_number(dna, nucleotide)`, which returns how many times the nucleotide `nucleotide` occurs in given DNA sequence `dna`.
#
# Examples:
#
#     >>> nucleotides_number('ATCGGC', 'G')
#     2
#     >>> nucleotides_number('ATCTA', 'G')
#     0
# =============================================================================
def nucleotides_number(dna, nucleotide, a=0, count=0):
    lenght = len(dna)
    for i in range(int(lenght)):
        if dna[0+a] == nucleotide:
            count += 1
        a += 1

    return count

# =====================================================================@020074=
# 4. podnaloga
# Write a function `contains_sequence(dna1, dna2)`, which returns `True`, if the DNA sequence `dna1` contains the DNA sequence `dna2`. Otherwise it returns `False`.
#
# Examples:
#
#     >>> contains_sequence('ATCGGC', 'GG')
#     True
#     >>> contains_sequence('ATCGGC', 'GT')
#     False
# =============================================================================
def contains_sequence(dna1, dna2):
    if dna2 in dna1:
        return True
    else:
        return False




# =====================================================================@020075=
# 5. podnaloga
# Write a function `is_valid_sequence(dna)`, which returns `True`, if the DNA sequence `dna` is valid (it contains only nucleotides `A`, `C`, `G` and `T`). Otherwise it returns `False`.
#
# Examples:
#
#     >>> is_valid_sequence('ATCGGC')
#     True
#     >>> is_valid_sequence('ATBGGC')
#     False
# =============================================================================

def is_valid_sequence(dna):
    nucleotides = set('ACGT')
    return all(n in nucleotides for n in dna)


























# =====================================================================@020076=
# 6. podnaloga
# Write a function `insert_sequence(dna1, dna2, position)`, which inserts the DNA sequence `dna2` into given DNA sequence
# `dna1` at the position `position1`. Do not forget that the positions are counted from 0. If the position is larger than the
# length of the DNA sequence `dna1` than the DNA sequence `dna2` will be inserted/added at the end of the DNA sequence `dna1`.
#
# Examples:
#
#     >>> insert_sequence('ATCGGC', 'TA', 2)
#     'ATTACGGC'
#     >>> insert_sequence('ATCGGC', 'TA', 0)
#     'TAATCGGC'
#     >>> insert_sequence('ATCGGC', 'TA', 8)
#     'ATCGGCTA'
# =============================================================================
def insert_sequence(dna1, dna2, position):
    dna1 = dna1[:position] + dna2 + dna1[position:]
    return dna1

# =====================================================================@020077=
# 7. podnaloga
# Write a function `get_complement(nucleotide)`, which returns complement of the
# nucleotide `nucleotide`. Nucleotides appear in pairs: `A` alongside `T` and `C` alongside `G`.
#
# Examples:
#
#     >>> get_complement('A')
#     'T'
#     >>> get_complement('T')
#     'A'
# =============================================================================
def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'

    elif nucleotide == 'T':
        return 'A'

    elif nucleotide == 'C':
        return 'G'

    elif nucleotide == 'G':
        return 'C'


# =====================================================================@020078=
# 8. podnaloga
# Write a function `get_complement_sequence(dna)`, which returns the complement
# DNA sequence of the given DNA sequence `dna`. That means it swaps all nucleotides
# `A` and `T` as well as `C` and `G` in the given DNA sequence `dna`.
#
# Examples:
#
#     >>> get_complement_sequence('ATCGGC')
#     'TAGCCG'
#     >>> get_complement_sequence('ATCTA')
#     'TAGAT'
# =============================================================================
def get_complement_sequence(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[n] for n in dna)
# =====================================================================@020079=
# 9. podnaloga
# Write a function `mutation(dna)`, which swaps nucleotides `A` and `T` or `C` and `G` at the random position in the DNA sequence `dna`.
#
# Examples:
#
#     >>> mutation('ATCGGC')
#     'AACGGC' // mutation at second position (index 1)
#     >>> mutation('ATCGGC')
#     'ATGGGC' // mutation at third position (index 2)
#     >>> mutation('ATCGGC')
#     'ATCGGG' // mutation at sixth position (index 5)
# =============================================================================
import random

def mutation(dna):
    nucleotides = list(dna)
    index = random.randrange(len(nucleotides))
    if nucleotides[index] == 'A':
        nucleotides[index] = 'T'
    elif nucleotides[index] == 'T':
        nucleotides[index] = 'A'
    elif nucleotides[index] == 'C':
        nucleotides[index] = 'G'
    elif nucleotides[index] == 'G':
        nucleotides[index] = 'C'
    return ''.join(nucleotides)





































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request

import io
import sys
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3MSwidXNlciI6ODM2MX0:1pKKwn:gwswLZUb2QZfZnRwGlguJmeJuet3AMiQPB65uMyxySI'
        try:
            Check.equal("get_length('ATCGAT')", 6)
            Check.equal("get_length('ATCG')", 4)
            Check.equal("get_length('ACCGGTATGGCA')", 12)
            Check.secret(get_length('ACCGCTTAGTACCAGTAG'))
            Check.secret(get_length('ACCGGTATGGCAGGTATACCGGTATG'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3MiwidXNlciI6ODM2MX0:1pKKwn:d76yhXyy0CsmVd5kHpd_fNp9o2UtOQ5O34auU1fCe-w'
        try:
            Check.equal("is_longer('ATCG', 'AT')", True)
            Check.equal("is_longer('ATCG', 'ATCGGA')", False)
            Check.equal("is_longer('ATCGGC', 'ATCGGA')", False)
            Check.secret(is_longer('ACCGCTTAGTACCAGTAG', 'ACCGAGTATGAC'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3MywidXNlciI6ODM2MX0:1pKKwn:j7ggqZBmbt5X6uMuXmgOnlinLGDu7-bzru45IX95stY'
        try:
            Check.equal("nucleotides_number('ATCGGC', 'G')", 2)
            Check.equal("nucleotides_number('ATCTA', 'G')", 0)
            Check.secret(nucleotides_number('ACCGAGTATGAC', 'A'))
            Check.secret(nucleotides_number('ACCGCTTAGTACCAGTAG', 'T'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3NCwidXNlciI6ODM2MX0:1pKKwn:zbupgwA0laOPBF19QHHbnBr82WDABNdHEgJum-XTlV4'
        try:
            Check.equal("contains_sequence('ATCGGC', 'GG')", True)
            Check.equal("contains_sequence('ATCGGC', 'GT')", False)
            Check.secret(contains_sequence('ACCGAGTATGAC', 'TAG'))
            Check.secret(contains_sequence('ACCGCTTAGTACCAGTAG', 'TAG'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3NSwidXNlciI6ODM2MX0:1pKKwn:L2Mn5Lz1R5gNoAzeGe-G4onKcvrCyY0g1BSyHLbm2ko'
        try:
            Check.equal("is_valid_sequence('ATCGGC')", True)
            Check.equal("is_valid_sequence('ATBGGC')", False)
            Check.secret(is_valid_sequence('ACCGAGTATGAC'))
            Check.secret(is_valid_sequence('ACCGCTTAGTACCAGTAG'))
            Check.secret(is_valid_sequence('ACCGCTTABBACCAGTAG'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3NiwidXNlciI6ODM2MX0:1pKKwn:0f4W9GzsSH8zrgx_ATkQeR3i6BmqeD4TcJoEcl8OX9M'
        try:
            Check.equal("insert_sequence('ATCGGC', 'TA', 2)", 'ATTACGGC')
            Check.equal("insert_sequence('ATCGGC', 'TA', 0)", 'TAATCGGC')
            Check.equal("insert_sequence('ATCGGC', 'TA', 8)", 'ATCGGCTA')
            Check.secret(insert_sequence('ACCGAGTATGAC', 'TAG', 3))
            Check.secret(insert_sequence('ACCGCTTAGTACCAGTAG', 'TAGCTAG', 8))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3NywidXNlciI6ODM2MX0:1pKKwn:d5Gky6IV6vUui8wD2AUukGs5qJs0pqpg87C1s2nMrPE'
        try:
            Check.equal("get_complement('A')", 'T')
            Check.equal("get_complement('T')", 'A')
            Check.equal("get_complement('C')", 'G')
            Check.equal("get_complement('G')", 'C')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3OCwidXNlciI6ODM2MX0:1pKKwn:s2v_zUAXRH5DjVGdYWYjph-Wr1WtFKUSwA2Y8hF0ocA'
        try:
            Check.equal("get_complement_sequence('ATCGGC')", 'TAGCCG')
            Check.equal("get_complement_sequence('ATCTA')", 'TAGAT')
            Check.secret(get_complement_sequence('ACCGAGTATGAC'))
            Check.secret(get_complement_sequence('ACCGCTTAGTACCAGTAG'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDA3OSwidXNlciI6ODM2MX0:1pKKwn:g4JalJAxD_9VJ2I5ULSkk1wp3mH6xdPJ6u_ruF67XG4'
        try:
            import random
            random.seed(8)
            Check.equal("mutation('ATCGGC')", 'AACGGC')
            random.seed(13)
            Check.equal("mutation('ATCGGC')", 'ATGGGC')
            random.seed(42)
            Check.equal("mutation('ATCGGC')", 'ATCGGG')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token aceb2f9d3932ead12565b6eb04279c4d89da652c'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = ('\n'
                   '-------------------------------------------------------------------\n'
                   'PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n'
                   'Preberite napako in poskusite znova ali se posvetujte z asistentom.\n'
                   '-------------------------------------------------------------------\n')
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Updating file... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Previous file has been renamed to {0}.'.format(backup_filename))
            print('If the file did not refresh in your editor, close and reopen it.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
