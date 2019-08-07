'''
388. Longest Absolute File Path

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
'''


class Solution:

    @staticmethod
    def lengthLongestPath(inp: str) -> int:
        paths = inp.split('\n')
        current_lvl = 0
        parent_path = ""
        full_paths = [""] * len(paths)
        i = 0
        bigger = 0
        lvl = [0] * len(paths)
        for path in paths:
            count = path.count('\t')
            path = path.replace('\t', '')
            if current_lvl > count:
                current_lvl = count
                # search parent
                if current_lvl == 0:
                    parent_path = ""
                else:
                    for j in range(i-1, -1, -1):
                        if lvl[j] == count - 1:
                            parent_path = full_paths[j]
                            break

            elif count > current_lvl:
                parent_path = full_paths[i - 1]
                current_lvl += 1
            lvl[i] = current_lvl
            full_paths[i] = (parent_path + "/" + path) if len(parent_path) > 0 else path
            # print(str(len(full_paths[i])) + " " + full_paths[i])
            if "." in full_paths[i][full_paths[i].rfind("/") if "/" in full_paths[i] else 0:] \
                    and bigger < len(full_paths[i]):
                bigger = len((full_paths[i]))
            i += 1

        return bigger


sol = Solution()
s = "xsfmnybyflzibrewmfpxeishyvrrybkqzyuvoehcyqupsjdwqxipeuffza\n\tqukdekacfnfbffvrierxupppsggiwtnzwzbspndj" \
    "tkwpvyazvuwryiqzarqxahndmbsmdoqdjbhf\n\t\thxttkicjbwaufxcjohukkikjbeanaprhalztwmirwgjufmuzwvkrjcxlao" \
    "\n\t\t\tbjklxudmjvutdvvfxrcmxhlhjfmxpnnljajiyykxfabyhfigcvytigjixprwfljxptmthqdatrywbhor" \
    "\n\t\t\t\tcgbidwlfvxvdrvgjgufskqgfiqenfamliftawifqbgvrj.df\n\t\tsmvuctybaatovybpaikdykgnfup\n\t\t\t" \
    "hifdrcspamfxcyisdgfzojctqovfuibwqyeacqimkreepbxxmaobdoknzsxpmixtwqgbaomjdakjiboxvfkzrshmsgnnztpefhdmkpufkpe" \
    "\n\t\t\t\tbyqrxvtcywrfqjfapcuyavsjytocsqjvqaydsokayrqpvpusocvtecpdijplxoeqwptojiqez" \
    "\n\t\t\t\t\tphevcaiegyjatazjlchdekyflrvb" \
    "\n\t\t\t\t\t\tpnlypaytrmcfpdrctoasorsekacbgoaxnxzfyagawlxblzgs.awotcscymhdfkpgvrgwxaubvmexortladnguaowueqsvrslpt" \
    "\n\t\tiodafqcbkwenzatberygzaxqtyqagliqubslycjfi\n\t\t\txxgqzwettztlsbwcpyvzwfvouadztghuds" \
    "\n\t\tzhaamlbteefxvfgeyqlclgemdvrlwzfipdzuzhkuzijuvplteftazxfebovibvesc" \
    "\n\t\t\tpequtmuqkhdeqmfiqzwtixejwkbeindqwgthhwnmxpalhcrimpdicm\n\t\t\t\txvwfnkuyokpdbdmzveskiojmloxaejdfje" \
    "\n\t\t\tblcxqhqnsfeipdmvrkbsjaxtludgpgkhvzpvqitqmmmxcduehzvorjlklohuoegkgkxmrmgcmjjbrksgvfuvtczvmuehuiohknxuprhv" \
    "\n\t\t\t\tmypptgogbcplebtmyqq.jcvqucyhhkkhuqmjhfbmsu\n\t\t\tshqnzstctvneimqovetwgjgdcmkmdjvcwqqqbijttkdvgu" \
    "rwgarexuhwwdtofdfhegwqqctrceqpqppbibsowrowrogxkceixhrhezvdoeqiz\n\t\t\t\tpxeofhoqmtnfxpt\n\t\t\tczvaezhqoe" \
    "grsztawyurvoisykkwbacbs\n\t\t\t\tvevxrpbktrorabkjqesrc\n\t\t\t\t\toepedwdqwhnfdagsjqfouaoebbgafxo" \
    "\n\t\t\t\t\t\tfxxuqfimrmlcapqhrdvlqxtpknawyvemqaayt\n\t\t\t\t\t\t\thscsnqmwtkerzsj.xxbjimpktyde" \
    "\n\t\t\t\t\t\trcccvisnnkdvbddhkxjgisfiyprahbahcqnuaqwiamcvcowjexcybtidoygftghlzfnazlisqvbdjyssiwq" \
    "xoyeixiaarkoxmk\n\t\t\t\t\t\txmhvcovzbokmrvuwjvpmezpychjcoxmboodvalyaivdfszagagznnkqrtojopakxlnliqrzdpulmq" \
    "pmfwdavmkny\n\t\t\t\t\t\t\totamcrfsrhlyea.poncevbxrlubqexyecgqfwloooqizyqjnggvyeuntn\n\t\t\t\t\t\tqjrjnfdgoywy" \
    "wacjwwsxxysbhtkigmctxkgqtwgvvckymox\n\t\t\t\tbwjpobitnsbtttubxegfwenxcylvuitcae\n\t\t\t\tearnonpgfobjlswpbmyjr" \
    "htdfemgmvxwfqezsnnwkdjummzckajnpogfdwfgoulnkcrfzntjkvqw\n\t\t\t\t\tnwpdzkjxgntcrupmcxupfignnesvkiyhuvzahycxnhy" \
    "muexgyl\n\t\t\t\t\tcffosav.qkiasvmflxidldmunaxkuyctrjkkgizc\n\t\t\t\t\thebqzdcfevwegdyyiqysnwhpivbubpiaercdd" \
    "\n\t\t\t\t\t\treakcufeykupejggvzjkvzfbbfnxoicpuehpwcukpayfjqdkswrrfidnurocgpijaymguoetnrchjwjcmwwrair" \
    "\n\t\t\t\t\t\t\tvhjordwfsxdkeshuedcwvqemmulne\n\t\t\t\t\tnjbzerdjaedmhkibbbbiwtcgacbnjdovtofshnltesulkegkiikbcz" \
    "fstazvylxuzbaswejehjlowydsgwuptphrdwmbuxecpqpkw\n\t\t\t\t\t\tytesfsautcpbwctiocopsiohwrlxehzjqqfobqtbhmobzfpvd" \
    "cdkfgzwssydolvfoknjgfncakbkytqiafutaktzjecwjvitzwqblfddhd\n\t\t\t\t\tjmafjmpoanjxmzopejmkgdoqqrf" \
    "\n\t\t\t\t\t\tijg.bbepnarykmjjzdxelv\niyijkrotqfllzviqliyogotkkjimoyiywzlppdqucjuozvcbctmkhghwbdaltisurnakkcn" \
    "jjbqidpbvzjmzvjgwzhuxqdjpffb\n\tkehcmvwwltycpicgwivvdfmlwhdivnemlbkgwzyoocavanktgrdjdvewroyoptfnfrcoohgra" \
    "uxrmirrad\n\t\tmswgowvttxjhzqzsbykbbqpjccnoyjuujdaxcycuwhfdlzdzguqbahgesldolsazeu\nlgrnlmsjtbobdqqwyubnpwq" \
    "oshvdokspgtssdaszrgzncecvxoxuaqxrvlwlaavhtvbdvvzclgzrgucfyigznbugmckgrr\n\twxpkqltcakmcxsvssyykbphfmwaecv" \
    "solauwpveckzjdrkhkrxqdqxgqxemlxqgfzwgvfinn\n\t\tccrqqbihnpnq.felbmahwnuzygcpskwepzwmmvhjqxopgpzcmujibymlpe" \
    "iaqxkqwcyxvunqdjulqj\n\t\txyanuidxogqfltdihpczzpnpkkvudykeugrpdbjrfdmdjflxurlblkiibfuieohulroarsmotonlmuqmg" \
    "wxdjkaqpkkehqdkidbcifdvap\n\t\t\tsreikpjtwdvnrnj\n\t\t\tbgffxxdmqgqetcwkhztvcruapodlhcwedxwzgbttqdgbsglux" \
    "\n\t\t\t\tnxcdhmjrlwxvyn.dbjdunnplerlqnvpkrdrnumjbqdpnapvcnhqoolgnclaewiovqvfirbhcgqxlgcodewt" \
    "\nozgxkcxyzbiecntuhgilgzerceqtlaardbqwmmkrejgjmjdyqbwsec\n\tyexaooxvzumffgttmhworazrnyrrwdrdavzgrjjvacavztz" \
    "dmeekfxbyiggxzihyuxmtolwchn\n\t\tekqqigbydisdjmdqexxmteeihmznspkdxhysir\n\t\t\txfxpgtrhzwzblib.fokzoawhotgqiyu" \
    "cdlmmeuuarragzaqmuibkssqgzctkmgnnwpdxslchaepons\nmtyksjsaywreruhujeniflfvwoufoxpceydndnenpodmmzantehkkxieumgygk" \
    "torgpbxiedofsiauymwirbfucmyr\npdnwrywazlmwlnqhydhonztzvljtdehtezxqnnimwdpejdxaucwuwzghniwdh\nyzhrlkejfkccpxzppt" \
    "glajyppdpyakopnlckjsgxcwbvepaalwzrvavebxskcbpdhxk\nznsenudxhqerznhcrxbnicwylenldxyzykrzdpepzmhekaqfcjietqnbrvoq" \
    "sviyndrnml\nwxnoufddvnspgjz\nawsaxewetiiijpsnvjtsfyudnvyecuhfejnp\npqyjczivzufnlefqlaigkan\nfsiwfwdroobnkycoajmw" \
    "wcfvahwsmubqfqaxttvvcpoiqgqyrumphlszlyqwhnvuqdfkbbcybbb\nupevhottmmcjk\niogrlydgpogiqwyocxxyvqclhfwruhtsqxhvvqf" \
    "xprzk\nlyyvnsrliwwdcmfbckbengrstwmdikdwundxsorplgtubdzhezlbfsjggydkfxhxyyikyeeahzoorvhwavlmkoxre\neyuhqonixeeqdn" \
    "rsdtsmzamvedksjigdtturocfhjcziyy\noemllsytiyiiskrxwuouwtfdrcxmbupydvjkpvteomhwxpeawhfiyghllfragdyehsydj\npaqyvjn" \
    "yecpmqydhvqcyik\nubhbqblxgikkskzuqrmhsolpvmyzbmvbrinobjzc\nictwircxfmbjalddybplvwpgz\nmlhdshyfmb\nuipplwljtwjryi" \
    "avdmlefswjvaochlzxbxuoecykwllpkizwhkyvnhanyliizpfhprie\n\tumarzchvaguahpfjthdohjjp\n\t\tciylqhejzqbklpthqfoyar" \
    "jvzgytmjudsjxuinxdhfjgyhbnpdggcuscbfgrjdjrlauuvnayraqtqitrfz\nshklyshqabstqpbgmuvvdfpqdvckupshebxhayvyrpxnpmij" \
    "edhbgtccjxqduayvxwsraes\ngfcfntkmjmofxznzacyzeybjbcjlhaphapfuqn\nearkcabnciaonngouzdmuomrqgqkhyuqpxqyryhrmaxpw" \
    "hytuurcyncxhwdrtsrcqvddvxjdsppxruvyywaagpfjvxsizaaexcakhifrrl\njgfphlsdocmxdqquxusflfzslkcnzqftbyvzfiqwqnztmu" \
    "bvvtokxedpvaauyyvcjefovwhecsdokiupplvxazkjnwgywjslejialxyoa\nkczvyunphmxlxsroqkdgvsmcsepcfmtsfsidccffxkxvdgzse" \
    "vmeobrobsvkvmqu\nhdfbfuauzkaohuxwewgyrecybeobxnzaijpubmxpcwctbcocohnifraklrrxugsrggnzg\nrccmsddidsbnfupkjryqyu" \
    "pekjzwocbshhriiyzsrykktaswpwapwqpbgsmqq\ngvakvkbjceksvwdnkxxejikgubddfgfakcpjwqxyzdhrrnyidcvbbonpctqxegzqiwkksn" \
    "hgqtyaejqobpyecrzlbxuubvtnkxgwio\nmxgiczcmygupfdvtnhxysclhcuaqamligbiglnotquyexsxcyoawozcqvvplnmmsdbaldszukrtkz" \
    "vilslwjxetinvgapixoah\nctxhilqwtvyedrgeqqrqkzleyignvfipdaacxenhcwrrrhemyzxoxjjpargmjikmlealwljeb\nslwogagwahqd" \
    "cvzjusdajaaarrndbqfwhojkuvxztlkogpijuwuwbczdyddbtlhsskrhejqczzd\nhdhkillpibshgjkjjvievlyhythrg\n\tiplrturrvuos" \
    "avkfpiibdapdbqmlzycwbgdytrtmwdnuuet\nhdjrolachexjqfaczblrqsbphqpiiiloeiabmvsazrcsncshgluedsggmavrnmlrnmgoev" \
    "\niebhuiarcpkxjbzjhsqdgtpkymetlzu\nhifxfdghrzdsrhchutexidvqv\nifyxiqneiskyfhknooqlakkybpflgchnwofegcuihmzadpq" \
    "iacusznmwifrwbycqtsymugfzanmnwfiqkf\nmzfozjfdzpmsygxvbnkufbyirjbjoqaqfhicozdhbvdsiarrogklpbzrgtbvfkvrgyjevxkl" \
    "lkburhflxhokqxxsl\nckujtwoxsbpxmkfgz\nhlxndnqkjfanujqemnwzxvflwtlacdbplegpifewtinutmuzy\nyghsukdyhqyiyuykzyi" \
    "pocydgkeldjlobwjgylnpaqiyibdncwohyipqtzykxskefmfenn\nfieeffuopjbbrjkzetxzmiaybkxwnoksplflinzlori\nonbpkrpstgr" \
    "fdgrvpqewxhjooewswpyksri\n\tizqntvlaojkzpzkqzkmfblohpnybrgvlhisdhwwsaadxmlmysjrxwcghjoskgaubikfthtiexzkwkwkvhg" \
    "amjigksguoqjzhldrgjgufrdj\n\t\tkschoevfbpovzlecpktkkdshpzvckrlyrubduqpkrszqzfeptqwegaptsarcmiaenbuueyfszzbpcaa" \
    "cpxmgs\n\t\t\tflrhsztlpfxjzwywtwewelnowgtimeflklocjsrewqmhqmtrprzizbzxsehxpmdrewmpodqudtmxpsujzqgzcjaskspupki" \
    "koxcc\n\t\t\t\tcwyforrbvrdlrdkrfbxbrmxaeetu.nwrsumqsjqrujaztrwpdsytyihyepmakzxpoejtxburkhesbqvjfowxmqmvdgsrlqf" \
    "msqqvykcpggkwxn"
# s = "a.txt"
print(s)
print(sol.lengthLongestPath(s))
