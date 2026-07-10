#   --------------------------------声明区--------------------------------
#   项目内所涉及任何脚本、LOGO、工作流仅为资源共享、学习参考之目的，不保证其合法性、正当性、准确性；请根据情况自行判断，切勿使用项目做任何商业用途或牟利；
#   本人不对任何内容承担任何责任，包括但不限于任何内容错误导致的任何损失、损害；
#   其它人通过任何方式登陆本网站或直接、间接使用项目相关资源，均应仔细阅读本声明，一旦使用、转载项目任何相关教程或资源，即被视为您已接受此免责声明。
#   本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。
#   本项目涉及的数据由使用的个人或组织自行填写，本项目不对数据内容负责，包括但不限于数据的真实性、准确性、合法性。使用本项目所造成的一切后果，与本项目的所有贡献者无关，由使用的个人或组织完全承担。
#   本项目中涉及的第三方硬件、软件等，与本项目没有任何直接或间接的关系。本项目仅对部署和使用过程进行客观描述，不代表支持使用任何第三方硬件、软件。使用任何第三方硬件、软件，所造成的一切后果由使用的个人或组织承担，与本项目无关。
#   本项目中所有内容只供学习和研究使用，不得将本项目中任何内容用于违法行为，包括但不限于建立 VPS 或违反国家/地区/组织等的法律法规或相关规定的其他用途。作者对于由此引起的任何隐私泄漏或其他后果概不负责。
#   所有基于本项目源代码进行的任何修改，为其他个人或组织的自发行为，与本项目没有任何直接或间接的关系，所造成的一切后果亦与本项目无关。
#   所有直接或间接使用本项目的个人和组织，应24小时内完成学习和研究，并及时删除本项目中的所有内容。如对本项目的功能有需求，应自行开发相关功能。
#   本项目保留随时对免责声明进行补充或更改的权利，直接或间接使用本项目内容的个人或组织，视为接受本项目的特别声明。
#   严禁将本项目用于恶意软件投递、规避安全检测、未授权渗透、免杀处理、流量隐藏或任何违反网络安全法律法规的行为。
#   --------------------------------祈求区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
#
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
"""
 ██████  ███████
██    ██ ██
██    ██ █████
██ ▄▄ ██ ██
 ██████  ██
Create at [2026-07-10 23:39:03 ]
Protect by 清风
"""
#   --------------------------------使用说明区--------------------------------
#   vx小程序 -- 海底捞
#   export HDL_TOKENS="openId1#unionId1@openId2#unionId2" 多账号使用 "@" 分隔
#   ------------------------------------------------------------------------
import base64
import hashlib
import hmac
import importlib.machinery
import importlib.util
import json
import os
import platform
import sys
import tempfile
import urllib.error
import urllib.request

__dpnrh9n89 = 50
_2a2cbc11c2c79a = [
    (16, 0, 130, 'cac5d9f6c2c1dac3e3c4f0a8e7f3d6cce9e8e5e9f0ed90e79dc2d5ec9799e0e2ed85e3dcf086ffcae8feee8cc7c58ff78181f781808482be838da7869baebf9786b7a5a7848e8d95e299aeb492aeaeb9a790b281adac9991a09aa7d983b6a898b8b1b2c3b1a58bb2d7b695caa6c74252323a2961527e5a3a5d5d5c69'),
    (68, 2, 91, 'GQoF7goc1d8Y8_PyIPoEJSj0_wME9wToAfAw6-8NAAz1M_n2Cw0Y-SkN_A0jExozJwIiFygVDQhGCktOSisOD1JWIhgmKUQcVhUgUiMxIk0zNFIpNkBZRm5lampqYmloWUg'),
    (102, 2, 134, 'HCA3NWkhI2VfOjw9SF9iP11UVWJRb2E8OTh8T09yY2p7WER1gF53YFZ6XV5Jf39kU35wgW9rhlhwkltdcXV-k5t1mZ1jfaCdiY-NemWKjnOSb51ssoS6m4-uja60w3u0k8KRwMWdsaPBpY6kqauokLvNn5GQxcTV3qff2cu8wco'),
    (82, 0, 2, '04603e610e610a023a071c1a3530360c1323541e270b5e051c270b5a1f2611452505001a0e0300080a072f32faccb0aec3ceeceff1c6e8bddcc7b6e7fbc2a2e0dec4f8fbc1cadbd8f2f8f7cdced5c0e4cac6eec99ac1fefdc7dcc3c6f6c6df8bd5ecc2d2edca8bebc4e58f88'),
    (12, 1, 213, 'ae949dd38faa83b88fb8905b36716c6c7c47436a49164d681a4f185a65557f511e09000c3c252a231829113d3130335b1f4c2e230ff4c1d1fabbffdefafdc3fcceddf5dc9e89e7fafbffedad'),
    (121, 2, 204, 'qMC8vrh8n8a-u7evyZu1y5zOzLmqw7qTyqPHucq7u5zQ3J6x0t3D3LvQvbrq6uC93evAzOWr1dXQydXV6ejuzvrV0tPju9fcvd4JCtIG5QDrCdza7fniEuztFfLx2u4TE_IR8w4WHwXk'),
    (96, 0, 100, 'f1bcac94ae8fbeac9884ade2bc89bbe2acb1b9e695809fbeb9b3ebb2a792d084ddddd2a3ad8a86add880acd7b4bb9fa19c9185cebf918294bfad8eb3594f547b54'),
    (59, 2, 204, 'c295Pm1TeEZ1iVNHYomFgE9jh0dtaGeKcHRamGyFZnNYkop-WHJ9mHN2nnR4ZK19e4eGsIuTsq-Mn7Oyt6N9l56zm43BvoOXgYaSmauGuKDKzInCoA'),
    (38, 0, 99, 'c2f9f8c3c2dae2faa0f0e5f7caa0defbaeebe3ddcdf7faedd98f92f5c0fc94def3d3c5cfd9dcf7f1d9dbe1e3f182efddfad0f9e38aff88a68f9296a8e8a7bdfaf19dbca5b9839c9fb39be78e85a0'),
    (115, 1, 71, '8a8597bbaf848f86a68fac9287cc80b483ab89bab5b293b04f6e617a37787d3a6d7752565468666e74735b54783b353e0927610232740429163c251c3f29360e4b17e8b3c8f0cfe3f7fae0d5f1f6'),
    (66, 1, 147, 'b48fa990d487aa888c94caa6a1d1b9306f6c7d3e217a545378174a77667b18747d5f550d2f73037309051a1f3d156b111f211b191622201331b9b6f0dbb8f7f3d3ccd4f3c4e3c0eee5d183e1ede8c9f18a'),
    (111, 0, 12, '4f45364b33b9e0e3dae1ecdfd1e2e3e0f9f4ebb8c2c6d3a4e9c1f4c7fdf6edc9a8cdcfdfadecf0eef6d2c792edc1c0c99acdece9dbc5eed481ccdc86d1ecebf4eaf7d5efc8f5f7fab6f0959583a2a8a8f2aaa28b9b87b98099edb0bb8df5a1b4eab7b2efe894b694b982bdaed5'),
    (13, 1, 114, '36edd5c6c8eba7c2a1f8e9ebe0f4efe2f780d8cdc3dd8983b7bf9ae7a4a5a1efb6b7d5ba8cdec1a3c49fa43645514c625a256c71637c794d66641c024778515a7e35337b7338663a32161f54561724211c26302d4c1c'),
    (1, 2, 173, '--IoJQsL_i8X_v4sBhIKMxgGFvklCy_7E0D8QRc5REAwARY8LCsdCyYYPiRRTEtNICYtGjAvSVReGi1dPR5kWlEzXyMzXDtZZlE_JnRlLnZHc1JxblxYUj5zYmOAOHlgfkRcZYRtZGB5cIFrgmOUlH92'),
    (90, 2, 91, 'J_v56f8nAggr9xAa9xL1F_cXOBD5NjY5H0M-GyNJIwdJQCtKJDMIOx8zOBI7NSUwVzoULh5OPlMxWzI-JDhgJldiLjlDXVFxa04xM0RHWEg-WTp_V0Nbd0aBY4p-WYJnRXdu'),
    (63, 2, 177, 'RUtaI0NfOEJmQTI-TE9dc1RMdHZ9V19AeUBPVl18X1GBi3xbdV2LWnpwXYZVkIuImZSMh5OIXp2BiGKRfXKVY5-nhouqap2lmpOOqw'),
    (100, 0, 73, 'd9ecc9f9f8c5ecc0f6d2e0f1c3e8d5c5f6eeeca5a2a9b2a993938a8eb1f89ea0ffab9cfdb78ab7a1bce3bdabf49e8a8dabad91ab94ac86a69181af86aaa18a988ebbd7808bbcb7c5c79bb48ece96afd199aca7763053364f7d3e53464d4d485e7d6b3b225b793e5d672e6f41574a5e5d726b65696d4b5a757d62711819477355664f19607f025645436f41007a'),
    (20, 1, 101, '322f47f2eaeacec0dbaca0cbdfdae790e8de9dffd1c1dcf2ac899ebdbfb3febab2b285cf8b87bfa0b096a3b9b2697a6e5d437c7c716e7d564a1c686d6368414f414c487400247a273726362a1c2453512806424b383a3d35eac5'),
    (62, 1, 130, '8f9182b1fdb6888790e9a980d6b6a1a989b4a18db29d3a4e70403f7f417d514e7a7b69406e6248185d6d5a28711d303f3a1c232071665501'),
    (43, 2, 177, 'UU1QMBc0Tk80Gk9gLzc2HVY4UlI6WGxiIW9aZUwxR1pRS0ZPT285Zl11PlE5d25WP1WEiH9-WoaLa0qRXGZjX2s'),
    (124, 0, 120, '9a8c85af9bcf83b1adcb99d259315759305548684b4555403c58636c5b407b6a616272205e5c5243444e534c4d4b60455d08616441784b4c564a7b6c61625e797701405e6a43587f6b68505c28137275220730313000212c013825236218631661210f2e106d191f2b64110c2b0728212b2b01282c04012c5e342c1f2f12281c24120c194d483f4c120a1326'),
    (88, 1, 97, 'f7c6f1fabc9aa6af889f8e8a8aa693b08b9ca485b7a0bfb4746155636f7f565752247552446d5e7d6b51657171250d301c3d22286c1c2a320e33222f2c'),
    (122, 0, 46, 'feede4e499ced9e8dbe0f083cdf6ef8eeacaedf9f7f1e9eca19790f088b7f2ae86ac88bb9c9b82a295bee5b692b88080a1b1ede28ae59894a991b18db0'),
    (52, 2, 183, 'ITNdHjpGNB8saEE9PjtiaU5NTW1RWVd7RXw3N2pBUoR6fU5mgHVadEx3RnVre02La3WEUWCYilt5i5qIi3aQop9ypKCEp6qTqmZ5rap9jK2QcHRu'),
    (0, 2, 64, 'kYeShndzm5yimpvCmY-XkMeSwbqVlqCYoaqrnZ2erqDGrNnU09WorrWiuLfR3OaiteXF68bEzeLXvNPw67PU5NHu9-q2ub7rtbu_3PHV3-jf0scHxNwHzPf63_3o4NYACdgQEh4W8vMVINz85BwDBAoCAyzl5w'),
    (101, 0, 217, '724d121924720e0e320c260a011e167f167d3d3e0b6a261133383b60223f6c281867382252300f272c10063e58585d1b2b22041a153d442f03054013143a3d481b18b8f8c1c2c0bdd6e6bdded2d8ffd5b7fff4d0fea6fadbf1d9c2c1e2c8c4d7f3f1e9e0dadbc992c0ecf8f6e7c3cbdfea9cd4f4fc8adf8dd981f18f88f3d390'),
    (57, 1, 226, '2d781254751e5c456c066d6a0d000f1b0c7a273a3c0c281250075c2229033c362b0ad3c5ebfcfadca3f7d6ddd2c1d2eaf19efa87c5c3deb4'),
    (81, 2, 171, 'Zi5uNjhkSUtad1tRPkJsgHNzQ4Z4WkiDdnmIdotzTGBTYpOIdmiFcpOdkVSOl22kjXuHe4Cmc4WuhqmEsoeRmpOFo4Khl294fYqdtJyqor27l7iDpIaov6O_tc2uvJ3MwL_Lo7WxtNyynK7gv8ra2sTCxLne6MPB7uHQydvwv8DMya71zPPN'),
    (116, 1, 231, '1c1d302f28323409241c4e3d16c5e8bae7dddac3bab7f3c4f6fedbe2da83c58dd0d5a3b7fe898be8ea838ae5928cb7829cddc4a485898868537c4b7b6224626d705b436f6c186f717b0076094a2e0c0a007d692c61397017130044410b4b304a4e16d1e7b0d5e5f8a0cea1eccd9aecd8f2dce3dee3fb8bf199af998b829da1'),
    (4, 0, 227, '83d8b886b8a4da9b9cbec09cdea6acbda181aa9c89a3bb888e46455d596f7f6d6167405c7b347f61627423415851775b7e737b6d765d2d51506a521b6c51131f43427318681e487c7b725040716246504169145c4e7f5b6c670e2f6f202c2402703a3a1e12743d09070f3c3c231c0f00'),
    (73, 0, 97, 'ecf1cfc2d9e1eadbe880dddeefe3ecddc088e4f1cbcd98a4ef96a0f097fea684a8b1a4f99aaab8e1b1a5e1acaf87ee9c949ab1a5ba9b8ea8a6b3a18e8adfae8c87bedc89d8a49ca0a69dc5ba8fbb959882c99b92bd995465754435282b5758615d634b575441536224495163594857702b6a7253285b716d55137b6c4843'),
    (15, 1, 125, 'fef6c1fae1ada8c59693ee9ff2d5d1f1f6cfa3b7a6b3a7a4edbdadebd2db8eabdbd8bba58cbd986a374d526a5e69514f68466c767b497d697e470f52'),
    (26, 0, 11, '1615754b1b6319671b196d4243577c717f7d077c085e64577255702a30087a0a0c751e0004102d3538230924673114113d202e2c0c3d1006306f6612163205112a1334511f'),
    (40, 2, 92, '_vv8vv6-988Cz9D_2fvz4ezY5gLo5AjqCwfh5wj50vz01QwQ3_7fEO8GBeUbBxUtC_b5GfD-ACn0IykWFTsUDDceCCgwQfwCQSYUQzM5NUo1RC4jKi8TMU0rODdUSBNIMj5dVGAvLTxhQE1cSGZKNjhbYmY5MCtHMUJEeW5ue11WU35wVTt0'),
    (119, 2, 136, 'dUdxZzBqXG98VlI9c3ZjWX9VZ1hKRYlNSmVqUk1vaVeKlWiOmGd6WXmKbKJhXpRvcmZho6ereqiwrpGOko1xlKakl7SriXjAeJiMucKknaW3fcOKosi2y8fOvsWspq6205akta7ZlbCu2M-5wqTF5Kjj2evU5rq9rrDv3cHV09Y'),
    (19, 0, 12, '2b4e4f634f665d674d1b7c686d4a786f7f5e01404a437005070d61400851720c75712b30260a0219081f283a1c7979003d6309'),
    (60, 0, 165, 'd7b589d297dfd1908183b99c8c998aaaba99a4c6a18e8fa0968acdbab6c7ae6e4d6c6b4e4c37657f666833746e7466554b7a2a5b5d4e744b4d6d4b50586a6a45557a51474751547b7f4f7d615e7d775866677a556c05440c7e427778695d69180a07072e2a2a2b192d18083b29631e1f3f00116d123c0f3f2962046b31013123093007322b'),
    (30, 1, 181, '89959090b6ab8c8ad8dd829282a099335369504959736c77222e494246421d731e7e6f5b6801747e0e02252c1d1b321005523b2a5e443c34362df0e8b6beecddcaa2f4d7d4e997e2ddd6e1fcc4ed8ff980a38ebb96'),
    (11, 0, 80, '6b241f06390e113b35532f23155f5c243f033b261b3d29044a321232013d2f1b0a1b1f2e1ec9c8dbd7c9c4c7d6e4dcd9fbef'),
    (106, 1, 48, 'f0e4eaedcad9d6d8e1e6ebebf99581a6be99b1bd84bd88be879389b180b381af8c9545497e44444040217a7d4d594f4658417e61577179080f132e1b7e13600d1e2f263c122a55074701280153dbeb'),
    (93, 1, 253, '2c700b5b52280305240d3b293db7c1e8dac4ffa2f2fcd8c6c197faccfaffdee6dffc888889a7fcb5aae6ac8fa68ad2b59ea8b19b9d'),
    (87, 2, 41, '-tfGxrr70v7r7b3gBvsHA_zf8-EEB_7J3xHhzRb-_-rn0tj65uoc2dUa1yAR4SQI-_7q_B4H6AvvDu3w9RUICRAPDBz99hw1KygAHwI4LS40QhoVGhgqDisSPxMORxAyUVUzV01HPxkyYR4'),
    (46, 2, 248, 'm5NakaOel4VmcpZkfI2ehamFkY2xmqSygLmul7x6d6S8oIC4gcKTn5-phr-_x6TPzcCvxKiMzJ-vw6yk'),
    (128, 0, 96, 'a1bba795d493b9b1b7b1a1aadfdbb68183b69cb8ada2b1b58eaca29e88cca1a844653345483d6d4b5c5f7e634e3f7465513c4822515d582e60'),
    (99, 2, 31, '0fC26dn-u_nc_eX40_PZ1gD37Njkz-oQCube9wgWCQkY3OfmGfER8Oz29hsWHggCICYkAAPvL-3uKgQSDyItKicrKScZLxgC_SD5ESBJERRERk0tDgpDDk8rVkMuLzgrUipSW0pTGjpgIx9lJ0ApOUtrRllCRWQxLDB1Vm5gZjF2TQ'),
    (56, 2, 137, 'GSn3HPYTQB4_QhQUHx8HNgRMPjohPy8FI0ocJ1A9PlUlFhgZLjMZLjNWZSRXYD5XY2lGKmxkUF1GdDBzcERsQXRya1JndlJvTHhyYWJPVl1hWkxgfG1kh4OLfklRd2dlV3RWfllTW6CVi4WQppibnnibe4SqpaGE'),
    (36, 2, 236, 'QFJsVWZMTH6GimZ-ZINmiWlweWeciouPWopwgWCco1yoZH2eqKqVcI2kgo1viqeZh3KQi7O0pZeTm7iapsfFyJeXvrKsnYPGu5ynjLG1w7mk0c_J0srQ3bSvz67Z4djX0tLVuQ'),
    (25, 2, 29, 'jIt8g520kIunj5V6cq1xn3p0rZZ6xcWuv5mWxYaptaKosM-uzrWQs8unzbDGytS9ydSpm7vE1dLI4dmhwOTJ6rjbw_PA'),
    (92, 0, 104, 'f58daba29e8bbbaa818ebda2b2a6e3a4e4b384eeeebabee291aeaa95a48caab5b4819cb1c5b98693a9bcdaa8a093a1a0bbac91bfb192b3ccbfbf8fb74764685769513262577e5541397c613662614d5276734244764353365b6b2d47535677455d4b6e4465457f1d5a6f577c5e694b5602536c58627f7f70495a'),
    (97, 2, 179, 'RndXinFnkY-Uk42KiFdnXIpsh15dWX93bWN4qKmJq6KbfWp5bKRqs4GpgYSpk6GWiq2cf42ofsLCnsGcw7-rt76tzomqp8Wypr_YrLSisds'),
    (117, 0, 80, 'f68db18babbf89a18397aeb692878a819caeb4e99894a296abb4adcd85d4b68b92cbab9f91b9bca1a2d7bf89a49c878da0819fcf80a5ca89b2aaa6374448647467755f5d7c5254666a403941237e4b'),
    (86, 1, 44, 'cbc9bee3eca2d2dfd2abffeef0ca94d8dd98f0f2e48982a1a0f5e7b0aebca4bdb286b1b2ac98a5b991b3535943315d7f24607344466e494d1918037e44546a77232830197d3f7900151f0e142a5e59250333414a34d0edc3e6f8'),
    (129, 2, 144, 'Poxhi1xXXod7km9-YFZ3ZnhZloZvoJyRjKOEbaScjpaGooKunXyRqnydjKmej5W6qIawfLeclax2jpx_krCYv6qdpbi9xLCcvbO-q7e2uJSkqdfNxOCcuNzXw7-hoaTjwt_FpKXrqM7s4vTewvDDy-Kzyd7v-vLg3uDv0PLd_cTc09sIBg4Q6uLo7w'),
    (113, 2, 218, 'kLS4toaIo52jzsnAz62mz46_ycOutaqpvdbZsNiqspu5xeLFweS05efF3s7Ixqvi1dDMt8X61bLQ8NP8AeL2z9gA8N0Ew97g5g'),
    (98, 1, 110, '83a6e5be8bbb90aebedcdbc58691a5874733413d5e7f685a59732f53700a44455f5a786d7b57761439381f33263a0f70173235013b'),
    (70, 1, 63, 'dac0dfbba9e5f3c8dfc6f6d2cb9bf5e1fa808bc7a4a58395afb2a9eeeea5b0b880ac8585a0a3ad93a84531477868574b4769295d14406b725a7460414e5045317c111d3e0e057a6b1f1a310a2516383610193f48d2f5d0bec2caaafba1aaddd5c89c93dfdfe085dddaf1aaf79d9bade1b08fb3878b97cac7a4b491acb593ac43353e3d5e482772704f697514'),
    (51, 0, 58, '2f3d5b2a27243d3514411a4821233532301c47cee4b2b2c9e2ebd0dabfe7cdfcdec2d5c6a4f0c2a4fbf8c1ccd8e9fdd7e7afd6faf1fdf1e6f2e5959bc7c2fde0dfc9f8d6c4e5c2c685f383effa97fdde8a8ccff0'),
    (94, 2, 48, '4MXXAQwCA_r4zuD62wEF3ub18OTw2_0XABEKCvkcHAb69CAVFiAc_hj_7SEdDgAeBCn1B_Yx-z4wNwpDOhEaMjw__TcoAw08'),
    (75, 1, 19, '0753522325542041062a392fb6e8e2e6b6c4f0a6f0daede5e2ede2f0fae781dff68ff79489ba98e0e1969de8dbb3bd80afa384b89d995431457d5e6d7e666d6f2a7e1c17644c7941704d7965722c211c272b3f3518370834323b3e3f131d282f'),
    (21, 2, 89, '18Sz66bJ0-23r9vd79zTwOTirePEyOza5b24y9D4vgDe3ufq-_TB5Nn96griDNTy_xToAhTr_vD36tUV3P798-TfG94oHggiAfwe5gcSJgzx9vMLPPgQMjUvDA'),
    (126, 2, 13, '7cX8wMUA2-jL9Q33-eff7QcN9wzgBOf22df_8f7y_RLfIf308xYE4ybtCOsi-ict7TUFCywHEwX79DsdFBsBQTwQFjcoKkkD'),
    (131, 2, 53, 'LSTwLv0uDDgx-Tf1Dgg2LTMs-i0QDg'),
    (42, 1, 37, '7b3f003f69261b550d1f5f33010e3e3708d4daf0bee2e7f5e1cfccd9f596fdf8fedbe2d2f4d08c81f4fd81b9859b929de989a6bfb3bc9ab2b29995446840417677687c7f4e276b6c46601469415d4e630e01060119083e246715040f3b15203a1a043f'),
    (71, 2, 236, 'dGGsoYSapn6unqBwnnG0e7x8mXiZrLaVs6a5tsWluJnDzYyXpLDRnMe1pLeorqOYkL7Izr29166xvK_AxaTUyKnrqafqzcnxzfDSwMnUytrL9NTnudXw_QDTAd70vdrj_vbp2uDpxt3g6wHOEtUb-u7ZEPUW8R3sJPoTFB8kIxEVJPcaCiQ'),
    (48, 2, 163, 'TEEHB0ALHUxIQD84VDhWRTRVK0UfS0w5TFc8Wx9BYz9nYCprO18-XGBVYUAsY0o7W1BsgD45dUxbWHlcU1pwfnZ6WEZQkWpLdF-CgohlloyFnpdbi3GeWm1lf5s'),
    (58, 1, 223, '4e4a50407f5d52427d41524f650c13160239261001603e150429031b242725224e513bfbe6efd8c9e6e4d3d5d1d4d3cad3ca98c0f8d4dad696aca38c97e4999ab2eabd8faca1a89ebc8da7b4cf516e604669382577724d2b1673416459565c0f7f53691a17310007303e65103e5410275d1b1b17'),
    (7, 2, 234, 'ZzNtTkM8L2YsbTI9VExuREs3bG5ydmt_WFqFgleIWGJWZkeAZlhHgGdii2ONfY5hg5ydmWaJd5GIlndxnHV7YXydoaprp7F6n6eetLF1pKSzuZq8'),
    (53, 1, 200, '95364841653b5a7c5d2d434e4955127e1976751b665e0c0813327338011f1d683a085552133c063907161304c6e8edd0c5dcaad0a1a5c7f092c0c9f686'),
    (95, 0, 236, '33291c1c1d31691a671a3f031b2b2a3b0d11172d383505270c1624215f3c015b310b37395a5d4815011845124401011d4d390c131aeeeaf1b3eac7b4d8cbb9b9bcdae8f6d9fad0db'),
    (17, 1, 177, '8d8afdbcbdb385e18b9685a98eb189acbf84be90a1463155402063546e2e2a687270657c4b6860604e522e74161338360b3a3e3d153231523e2443251f4d1d'),
    (91, 1, 26, '340c142fd9e8ebd2e5fda3fbc9e6fa90e29efac0c0d7c2efcb878fa98b86bb9a8f87e3efa2858abf81b895c490b18970706d5d67227774566c707c451b5b41700d41094976343e'),
    (89, 2, 208, 'fmB4npNvmXJkX2OaiqaBp6WyqKZto4eBo3O4pnKMuLWtjn2NkaidssqrwqK_rMXMkZ7NjtWSxce1lruXs6_K1NPWxdHXxrXint2_4MzP8dzG0cfgs9Xh9OLX8Pz-6ui_z_PO-8He5wPaCwrX4cb48vHnA98P9fP68c_k9g8b_RgiFfM'),
    (123, 0, 197, '340a360b072e7e240b0b7f2775783c1c270b1b23061712053b6f1f311f0f3b00212e5425315130112d332000293f2d002742342524040c3b13093b310a163452c3c7d8f6f3bdb7fef2eae1c0b4eabee0a6f8bfe7a3dbf9c0d4fbd1d8a8dadce5ffc7cd9a9794f5f7e7'),
    (28, 2, 174, 'Gvg3BRgYO0AFOx0rQUM7MiIMSlJPRU4uRlxMR0wrPGMhN0QmH0MmKlgpW2E5LCgxQC1sMlVsSTIzaEZfalxSXoBfUnFAZUNIRnuNjYRghA'),
    (103, 0, 57, '93e5f2c0e7fd93f1dfdafaca95d7e8fffac4c5e0f6db8fd3e288efeff1fb86e6f09eb1a0ae91f3f08d82bbaaa8f4aaffa0e49ca3bfb68494f5818288f18895f287a396dab0a3979f8b8fd99edfd8a1d9dda7ca90d990a6b98091929999ad8a95655241466a6f726e4f40'),
    (32, 2, 227, 'OlpwN4B5bk9OU35tUYBoQ4Zjfmxad22TYEmCZFJWZJRvWYdnal2Vl4WElHaAfJypeqZ3l2ykfIuIop6Qc3esdXutppe4orq7vLilwqXAksm1x7aLmY2RzpSSlqnXsQ'),
    (22, 1, 72, '3d231710595a3d043f4d1426fae0c1c0c1e1def0fccb90d1c0d09fea82dccae2faf792b79092e0ebb4adbb8a89afbcbdba9aa5be8cc849647f5f3f7e7d714f5c5a436870417d447c73745b'),
    (14, 1, 172, '89d29a8cf4ab81bcebb68ca9aa90dca8bf8591bfb8d49db62f6a4541625662222d58771b674d6e6c536d776d5630291839082a296f1439720f32253829483b473c28eeb6c1d8e0bcdca7f2ccafd7d7f2e1f8faf9e3e0f3fda1f580a89b999293b08e989682d9bdbdb9bcd594ab694254323f594771547e65497a4962786647026a481437777d063a2634'),
    (120, 2, 43, 'BxL77PccAAIeF-7zBifp5hQsDSgDIgn-_AQNAfc2Bij68Tf-DTU7FSMWGTYCPD0DJCUYRCVRRTAuSBInLFVZUVI6XB8aOFJVY1A1L2lVQGpbLThLTnIw'),
    (33, 1, 233, '58634a645b716c4041727b6f7e687379727b75227778000e37252910110b2601065f17144320161bd5e1fffaeff9edfde3fec7d49ec799edfb82e0edf8f7bcf499bc9eea949bae8dad9f8bbabd9dacc6b7cf623a614c614164225f5159597449697d5b6a437f707a0177221d2f3d620d31081133311f152224'),
    (74, 0, 81, 'd4c9def5f8d0d894c2ecd2f597d2cfd9e4c6fbebecd9e8d4fde5e5cee1c9f3ccddd78af9eea3998ab2f79cf792fda29da7bbfa818083a1e4929be38981a0ad9bbf9184a987d698a3'),
    (83, 0, 146, '959fafbf8a9f99969db8a494beb3c59392bca1cd97b5b8b6a2a69b786e436b334f513e40386d65426558564068637a2d5a6355545f7152662f6e2b6b4361755e7a770a606f4d585c1d746c576267504e47585f7d72600978717f7d32'),
    (64, 1, 11, '327d041d03630252090a1e55583c451b0c0bd2dccbf2e7e8a0ece1e9aae7d5feeecfd6d1efeded9196a091fdf8e499a0e884a5d0d5b8c0a7b4b3a999a06e7172323f254b464d7f6570671a66755a740c4b59761572013f212b22330311252645521b221f284a0eceb3efcfa1eef3d7ecaafbcddeddc3fbf4f187dded'),
    (6, 0, 175, 'f7f0e38b8bc2f9e4cdffddb091b490a9f6b4ad8aa5a4bd9895f6feb3b385babe928ee5bbbb89b2b1e894ed92d2b4d693'),
    (49, 0, 40, '1d0d3117080a3611552a1b0350322c111147051e24262c393c2145403224244e164816454b0e1cc9cff5b1ecd1c7ddf0f0d0c4fcd8e2c8dce7f0c1cde3e0cfcef3d9e8f8c8fdda97e3d093e7f7f6e5919edbe9e194c6ca86e8f5e482f0e9f1f9ecff8af6f9c7cd82a2f48785b7a78087'),
    (41, 0, 31, '2a3b043c0f2f2f7f0361391a1f320707150c2e2e1e10666b104c17212d335308222f042f061e242512054703310723153311490228293d25c6ccdbe6d6eeabbffbd3e6e1b9e2bfc3f3e5c7d6f0c3afe1d2f4f6e2f2ffe7c9d1d9fbc6c9fdd1efe7dfcecde3f7fcfdfc89dac099fcfad0d58e83e1e9f4edce9880b8b78e8ba7febb9e9e8f86aef8a0bae9b5b0b7'),
    (72, 1, 100, '9498f1f4f08fd197a5a28effa38abc93948c878f9fddab9084b8bbcd4d66334b4f5d22735e7a56431163077d01775743536c283224197a1e1921313439564b0236234b5849393fe4ccefc8dde6df'),
    (27, 2, 210, 'Y0RQQDonKj5Ma0NnX0UzSz5kcTlbckdRa35KczljUFd2fVNvVUqCaoBna2mRf4pnhmqKhHFsVXiUf3OZf3aCpYJ9iWShqXl2aamtrKVqa4GJsXQ'),
    (55, 2, 87, '59Di2_vt-A3ZxOgQ594H7RXp1_bp1RIN5xf7C_UiEfEb_fIeE-n9-hcfGwYzJjTq6wkOKjT7NR4lFydDExElJj0nO0VBAD4lTyg7KT0xHjcrElBVTFI7Nk9SMVZgMT1AYGEjWFFVKUdLWi5YUzNJMkNqSVhnO0s9dk07XTpuTmxAQn-FfmBcYWiFhQ'),
    (9, 0, 224, '839f9fa0a5d7acc19496b1aca79b94bb838f938ad0cdba3056743b504b504f5e3d334e546f43797e79796a764c43756d717b'),
    (67, 2, 205, 'RWqBTGViWl9MXHN8jlNfb5RnhI2DiZGAXHWVnoGDlKCUlXh6hHybsGyFjnOiq4-Lko90p7d2rovBsJ3Dmb2asqiSqLeuqL67us2wkdDUoNfDucjGvpnds5qd2dvAs-i3ycW4x87Fo_HAxK3FtNXSturkxtDJzM7dv-v_'),
    (78, 0, 79, 'eecee6f4e2c1e7fefdd1caeafefbc2eff2e3e08983e684fddddaefc9d7ffc2dbdceddc94a7a692839c87f0bdbaa0a085aea887948b90b485a5a7bd80bfb3ea8e91b5'),
    (2, 2, 166, '-d_dARfz-eLp-fQcKAj7DxImHinxLSQXODEbGxX7BwgJCgsSPB81PyYJNQU8PSNBLQspTBIqSlZVWVUzTFJJYUBVIFxhM01IJTxVbD1pKlwlXHFMMlZVNVNSXG1STz9-aVJacTlhRHJBaoJ2YVdLZIJ4j4mAaVBXWWWRU52KeaFboVqDgHWdoHyKnJk'),
    (105, 1, 232, '1d6c6e03242a10105e160d4414102b0ec7b0e8c2bce7dca4e1a8ecedeaffce9ed5feeef08884b5b5a0ab9595ec8890edb5a7afa6d899a591ab9e906c523c5c3f6353402f2a51446f185c655b0215706819030a7e7c1e1c0f6e2f2934230c115848310d0a14b4ebcbbad3e6fcf8f9ebc1d2f0c2d09fe0'),
    (69, 1, 10, '3d6b300b0a383b2d222723261e3a080f34d0b1b0b8bccbfeefd2fee1f691db949dfcefffd4d9a3968da38ea7aaa3a89a9c8ea1bf86a0878692a9c4696a6c7d5c64747a5e5d64424b575919005458555b4f18017b391d046c1e6a6e182a2f260d161b34002f27d9d6e5c9c7f6c7c5d0ecd9c7d2cff8fff6'),
    (109, 1, 240, '27243a372436263c3d1c310dd1cbe2c5e5deebc6f1d5ad94e49ce6dfd8f7c08bd9958da78095ffb3b28abcb6b1d5829abba38aa9bfb1b447546b7e46765040487212496b6b14556140757a5a10132f07352738033b242616155d34181d383a1b0fb1efb4f9e7e6c6daf1a8e896d3edebe6c8d6d0dff8eaa586f18d8696b2b3a996d2908d9bb8a095aa'),
    (24, 2, 83, '47amprDPvtngq83hyrmuwur2rbT538nY6_TI5fC82NPd7_be0PECyMkCwszczAD5_wfOCOga0eno_NIP_vcK_dwi8SAVCADfDCv7Ai8bABAtISgmCvHuIQ0HDPz7KkP6-DYPRyI-SDhKDT1PKVEOHA'),
    (39, 0, 43, '3a3e6c2138052e200c1c182b0614352a3339132d2e5f24205e343d230b5c4222000303361a1f39173d2d4a39343ab0edefd1cbb2fcd7d7dfe4e1d8d9e8d9d4e8f4a4a3fac0f0f0e0fbc3e8d6f8f4d4f396f5e5dcfc96fbdcee92fde496d6ded687ff87f8f8e2d1d6cffee9d8f6d9a49bb78194bdff98aa9c84a59eaa'),
    (79, 1, 7, '3a281e6e0e141d3804270e403c4bd7f9f2def9e9e2f2f4f2c4f0f3ebf0e4efeae9c3f5cb96a6a6fa9abbb6e0b9a4a991a086d4d9bec4bccaa7373063446341274e782c4b554e'),
    (34, 1, 100, 'edd9e4c2fde0f4f8dac8ef8ae3f883e7d5e9dbf8f680b0e68f80a68690aab1b2dfbea499b6adce99af7265727d6b597f6152735e46494645'),
    (54, 1, 250, '7d5b72144b51261d7119781c79662d052e2522285f0b06373b3d2cccdcefcbfca5e7cedbe9f0eec390e7f482edd2e88fafb3b7ffa483b686e19fbb98be92b3d8b387918cbb8955304b58605659636228121b496d1402507a09684c320212791d686b15153816001700392a1e46221e2cefd1b1f9e8e9fbfbf4abf694eee1d2c2d3cbe4e3faed9aadbfe6'),
    (45, 2, 113, '0tYTFNMa5vgS-98Y-vkgEAMHIBoeBOwqKPro-yYeEjcxFgv5Mwn4GA8AQR5BLBwCOTY'),
    (127, 1, 230, '35032f381413430024e4d2e1fcd4b7c0b8cce3aee6e6e6c7fbe19ec4cedfc79597a780f696e59db391d5a09198ad9fa18cbc8ebc343c4a4b5e4764246375596a6d666369786b450c6e0f2c0f79072a3e0669286a2a57571d5b381a112e4e48eecebebecfd2c3fedcc8eec9efe4fecc85fe958ad7a7a3'),
    (44, 0, 95, 'bcdfdaccfec3c2e0e1f2a7e4e5ecc0d6aafec7dfa9d49995e6fbea9f8afdf9f3e3de9cc9dbe6fc8a9edcc580fec9ecf3c18ed3ddfdb9f59bb09390a0af8eaab3a898819daab1b8a39ce0839098e0bc8e8fbfe990b08bb3868cd7d28a8d8ba2a2aa80a8aa9b94bd829a8291a6a0c0b18db084d0ae8f636533376f73496f4051674f53'),
    (110, 0, 251, '0b5b242d2c0f35261c1c424d38193c3c28030b2a34312bdae7cdeef6efcefde1c1c0ffbeeab7e5a9d2d0e6a3ccded8d6ddadf9e6eef4fbcbfee7c29dfdff8afcfec3f281e1cfd6dcfae3d18585c0e7dbefe9e9eecf8dd5f7859bbaab92a88c828684f986949bf8a58096e2b884fbb9ef'),
    (23, 1, 125, 'e6c6a9aaf9ede5facefff9ffd7f4fda7b391b89b83aa828a99bed595bcb2d9c7a6b88f9851484b44695c7e61486a57674916751d065d78610f7371236531221b3d7a170d165b'),
    (80, 1, 224, '62027356657c30131e2c782718213111160e0503053d032c3a0d1bccf1ffe4b9d6c3f5aaa9a9f2eaebe69bf0ffdbeeca8db294fdfdaae2f888af9797d39f928cc4a7b7af978671307e5e6c56767a2e70784e4a4f737b6851755e6b28736a'),
    (37, 1, 118, 'fdf4f5d4dffdc0fffaf1ca8adcae89a0bca1bde2ada98797949f809e8693a6b98890644c423c4b78493b762d6b47534d5d686361035d5b3a091c11070517786c6a6e075434595c381846334a4ee7caeafad6e7ddc1f2df8de5c784ef9cd9f4'),
    (104, 0, 5, '1e58421903283e412c373a151f0e381d19331dd1cec3dae5f6ead7e0cdfbd1dbe4c7ede4c9eaf4a7f0c6d3fae9d8d6b1d2dcd3f5e5e192c8faf1f3edda9fe99ccbe3e89d85f8f8fa82efe7f7eb'),
    (84, 1, 47, 'b7e2bee8f5c4a4f1ccf2c2e0cce5d4df81f5d4c9db839a91ba8be79fe1ef84acbc8eab838496a48cb28d3334697b404065435d576e511360465a5b037b40501605113b042217260a0d6e2615250000174b38110a3cc6d4fccfe5d9f6c6ced5dac1d4e8c2ddf98defc88f8396989888fd9cee9c97b7ac949a8c8997'),
    (108, 2, 36, '4_fqANjo6ADLDt7f_v4E_hPa8A0T5xEPCQ8Y8A4i8yARHd8tJwEK_yL7IyYJHjUCMC8QKQr9H_w6LxwEHSf_RQEpGkIVBxkrURJAI0BGFSw4L0gqWzQrTEw1WlxaR0I0ZyRXWUVWJmcpMkAuMVdkQmxgWHBbX3JNcVKEXW86cH8'),
    (10, 2, 24, 'WYuenJ1yW5t9dnOGpIWWn4ONfYN3rKWQbbOhtoF3lYm2qbOTsK6zn5yXtcKeurm7n6eEm7iKqNKkro6KlK2YlcvcmZeu2t660M3UueDXsdzAwMDbxbzL7KvJ3t_TsfXszfrz8tXZydPN190C1dzV6NjAxeD8DuzQ5w_d'),
    (107, 2, 239, 'wJzB1aSvtZrJr92csK6p0bXexNrapenS16PHwc3AxerH3fbWyeDLuvr06Oq81uDszeHexucECgDk9dfM-xHx8u7hAP7o6hHi-A0X2Bz5ChMO3u4B9fom9ejrH-f5Dhv_JjDsLSEV9DMEDSkK_Ao0IRU1FDEkAR8'),
    (8, 0, 93, '292d3d510225211e0106561c0807114107242e1f09360b3a071b3cb0f4f8cedcd5d9c3d8b8e2c1ebbab7e6a3c6ebf0fea2dea2d1b4a9c9c5fac7d5f1c0e1c6d2e6f3cdf0e1fffbe3c5e2cacae882f6d6fcd5c7dfd88b83ef8acbc994ecb0f7a284be'),
    (112, 1, 145, '776a5e5d3c547e24285571514a705e6d53584474750c0c300606226123282a3623085f2d1d42251054324aeadcbcb2d9f8cda3e9add390c9d1e3e687c7fdd1eff0b096a5e096abe7969fe988dcb2'),
    (50, 0, 162, 'e4b4e3e4b7efe8acb9afa79d81b9b5a8a38e8e848eb8869ea6b9ab98809fbc8296afbf91d5a3acbe8a8aa8c957514e5636376e495f7c6b515f637e7a46'),
    (118, 0, 104, '89bd8887a596afd5d2a18f9898a7a3a483d6ddc8cabd8392b5b5a1c8cfa9858b8d8d7148755c4f7269366d62666f616f7957267d275a5667747b77497c55786449327f52744b6a5361537f477a4976195d6053447355056c5d654e7b78425d59716a0d36003b732d706a323d1d3f017807'),
    (130, 0, 229, '3d1b3a02123b590f5628153d1140381d1a20173f14370b4a12daccd4c7e2d0d3c8f0d1ffc7c9cec5c8a7e9c0f2adf4d1d8b5c3d4d6eef1d8c5e8f0f0c5e6e1'),
    (31, 0, 108, 'ced8dcfdbdf9c0def6e6ecf7c3eadaf9c3f0cfcedbc3fefad9e1fcf1c691cff2f3d5c9f7ece69ceae1e3faceffd4dad6cef2e9fbd9f2f2f09cab93f486f0a8a29afdfaa7aa88ba839795b2a1b6eab3b881ebac9befd1839aa98fbd80889ba399c6bca2daa7a0bfb3a5b0c6b8cf88c8cbbaa5'),
    (114, 0, 126, '92939597a1a2bfa5a2818ca395b6ada775434b49775f685078456273763d786e5b4e685e6d625766537c4a79315574666f561747736c414c436f6c526b196877476940777965476f004353504e57537e2f26230130092b771f18023e02793e213c01211e361b6539370f6918'),
    (85, 2, 103, '_wkHJQ0NGBg4PBD0PzE8AhQPERsXRB02LDdMQBshBz8oVyAyJEcwRDI_RTQhWkFZQQ'),
    (47, 0, 131, 'db8299c68183ffc1f2c3fdf6d5ec91f390b1f6ad88a9a2859dfca6fbb9828780a5e5ed989b8fbc91e2abadafe8a8bf80bad68286cbd392a083d29680b19ac090958badb78ea791889ecb8b90b7b859454e754c42475f7c485e6a4a62374c7921534562257e416140697e64287058426b63494962766f'),
    (61, 1, 96, 'd196eef4d9c1dbd7cddd8ae1a7b3fe81bbb191e393edbbbaa9b8888c9382a7acb944694c447f622778415958116f1773747a7c606f6b4e38261e18213f21226d0904340433043a41031c3a06efb1ebe9e6c1cbfea9cce694cae4deccd3d9f2c3ce82b4f1bc9ff8b8afe0b799b28d92a9a4'),
    (35, 1, 87, '1b14f7c5d5cce4f8fcd7f4cbcfd9c591cec2f6f6d3cdd18987b28fbebbe69f9ebf8eadba87bfd4a1c4a5b58ecf7671494b4448717250532f45706e5c586961750b792c2115790b7f302230212a5937335c243e1b040a4b2fb3cde6b3c5d8f0d0e0dce6d0d6e2d9dee4eaf2e9d78c938ef3869e9c94e88389b8898b83b6a5c6b8'),
    (77, 2, 53, '2-jW0OzZ9LzSwd4H1bz0_Afg-OsN7NoRzRQS6Ovp2AzuHPbnFCHgGRTxBuQR9fblFwHmJQXwIAXs8y4ODCklICMc9Qgg_DcP_hoYRiVGHjc7Bj8CRS4ZPkBVEzZNRUspMS4XVUxgPEE5VztfWFo7R2xoZ0RlR0JYW08xXFhTZUNJcUUyPz4'),
    (76, 1, 71, 'd0f9ebdbecd8cfeff1d8e0c5cee8cd98a8bfb0b8bb8ba196848eb3a0dedd879ea7ce83c59d576b637d6f275062527864691e7a69614a575e6878092506291e1127336c0c0f38141c2c5a1d27073412edf9b4dde7d9f4deaed7a6feecc0eec5dad7dbcf8ac8939a9a9af6939c9fefbaae8e8fabd8a5b7878dc284335448796c'),
    (65, 1, 74, 'eeecf7a6c4dfadd9f691e1cbcdc0ccddefeef58db7858897b6a3bfea969182a1b9a993c098b9ca443b42636a76564f6a4177706c5d5b4f5760066c4f496f240c012061'),
    (5, 1, 170, 'c7c0f4c8eef9f9b3b0aefa88a3e0b7af91bbbcaebfab80a3c4a29f6f7b7e41445e74432e43705641741f6f7f6773607f0f08233d3b371805663768353122060d17110f171532d8f5c8d3e4d5c3f8fae5faf5d1def8fb88ebe0ffeeb3a2859398bca2988f94acb4a1a9d2'),
    (29, 2, 97, '9LfSsrm58vDK7t_6t_fDA_gGCdPJxvfq5dva2_vk8ODx8ArsAwvREOcTE-EBFxAXBP4hASQU9ikfIRLwDjUrKwUn8xn3CTr7Mg0XEwIfFxIRNx0USxs1RS5NOjoHS01JN04sLjsZMBI8VB0bPjBBIlI2VUtZIytdJ01FYWQ'),
    (18, 2, 197, 'RjoGHUI-SyROQxQlWzNXGjdXQTUzZRomIzJCZFU4XV86MWE8NEVAYzFzVTs2fTxcaVlZeFNdckVaXVd-fGVdgI1tTIyKUY-RgVJ6a52be2tol3SZpXRhfpN9dpSb'),
    (3, 2, 43, 'fo5kgotnmnmbh46Mp5Ckr4ugjKmJk7GemoCagLzBnZuGmLt-y5e2nqWvntKdpqKr14youtHcvrut0LWZwtPat9rhu7Ofo9_byOW88M6zverH7rD07NDZ2t763_EBAPP40MH2_cTo3v39-P4B0uPsEeIDERUK-ucSBekHHvPx2Rw'),
    (125, 0, 172, '781a791f6a4675496b4862444f42416b55427c5565556b37742776083711142f303a220f3e2c041228043b6706352631140268280b2e692b2f2c2b2b071216025e0b0f005e3d5f3300084b372a453f404c1f1e')
]
_0x4212bfeeaea = [
    (1, 2, 210, 'QjU5O0k3P0NJQ0JQT1JKUFcGHwgaHhkcHR0mUlAlKiNVWVhbKlxbLC0uYTI1OTo3OzhoaW06Pg'),
    (5, 0, 56, '090e0c24762126222320777a7a2b79787e7c2b663337656d6565653a7b76792c'),
    (6, 2, 78, 'zcm-xsa40MDO0MfOzoOchZeTl5mKlYzd4dvi2N3W0ebj1Onf2auvsZ63oKH9'),
    (2, 1, 124, '5cbba6e3e3d2f4f2f9f5e5fed2878489cc85d0858b8af7a0fea8fbade6e6bce8edd7d0d7d3df9192c49a9d9c35356b382c2b3673734252464248434310191a0f06707d7f727c6732356a653b03560c59574615454344e5e5e4b0b9b9'),
    (0, 2, 16, 'izN4goaCd4s6UzxsYm1hUkJNRIyXmJuMjIiLn05nX2ZoZGllamxqaGRbpg'),
    (3, 0, 173, 'd4d5878a848084d58fdf8e8c8c8b8cddf5f3f3f2f3f3f0f1fffffdaefa'),
    (4, 2, 47, 'bGuZWGNaqZu0qKyfo5-0qqR2enxpgmuDg4KBr4C0hbi5h4m7vbmMj42OlsKUmZaUxZzLmZufmaKhnqQ')
]
_w_3293f17b64a7 = "33d5f6e690abf5fdc83ce8e808ca75eff87a18abdcb82ea06d2442dd1e549108"
__h994551fb4a41 = "9864a1d4ff34efa35229d5952b8f34708627403d7cefff023a2432d6be69032b"
INTEGRITY_SCRIPT_SHA256 = "1f0e6cd6011685fb59401259b622bcd1de081de59e68efca03ee216152b7dc86"
__fjcofda4q28fiig = None
__2xthtg0m7npuxl = {
    'o_253f3da4a': (2467, 0, 13, 'd8c5c6c3c78f9998dfd0ceded993ddd0adee90acabaeafa2e5bea8e69b85e1bcbfbcb78ca1a6b3bbbdaaa984bab4b2ba93ce908293ca8b869b9d8f99c39e8189999d97'),
    '_v7c1bc7d233': (3124, 2, 101, 'CRPeCwED7xIQFggHGQ'),
    'd5d5cda9796a77': (3828, 2, 158, 'BAgC'),
    '_3h0wr3iw': (1214, 1, 213, 'a3b8a8b3edc7cdcbc5dbd0d89acedea5b7a9bb9caab6ba9ba2ae'),
    'IIll8989': (3515, 1, 215, 'ebe7ecf5fb'),
    '7f5fbae72d3dfa': (3456, 2, 220, 'u7zLwMnPwcI'),
    '819408acd91657': (3241, 0, 233, 'c3d5c4d6a5b9'),
    '_g6ffd56e6': (2683, 0, 223, '0b1d0c1e6d'),
    '436be8b281c6b6': (3791, 2, 116, 'qbO3s6i8'),
    'c3d46198cb9a48': (3266, 0, 60, '8e9e796d6d62605a756f693b3f3d'),
    'l1l12685': (1528, 0, 202, 'aeaca5a1a3b597a0ae'),
    '9cf601c87b49b6': (1946, 1, 239, 'fde2e6e0e5eafef9cfcdc1f5dfd5d7d7d6d0'),
    'Oo1oae40': (1444, 2, 243, 'B_kSBgr9Af0IBA'),
    '_oou609a9y9j': (3941, 0, 235, '39222126313109362c'),
    '0x51d6b3059': (1559, 1, 229, 'caca30646078517e67487f704957485c5e')
}
__l0a5d85a = {}


def __gpwecvbjnkt6(_db0ea0e327002a):
    return hashlib.sha256(_db0ea0e327002a.encode("utf-8")).hexdigest()


def _0x5743a91e(_o_7419ede06, __pc32d8a01, __xe47c54ad, _acd58dbf8983a0):
    if __pc32d8a01 == 0:
        __00gs2xkr4we4rv = bytes.fromhex(_acd58dbf8983a0)
        return bytes(
            _db0ea0e327002a ^ ((__xe47c54ad + _o_7419ede06 + __io6im9qbbw) & 0xFF)
            for __io6im9qbbw, _db0ea0e327002a in enumerate(__00gs2xkr4we4rv)
        )
    if __pc32d8a01 == 1:
        __00gs2xkr4we4rv = bytes.fromhex(_acd58dbf8983a0)
        return bytes(
            _db0ea0e327002a ^ ((__xe47c54ad + _o_7419ede06 + __io6im9qbbw * 3) & 0xFF)
            for __io6im9qbbw, _db0ea0e327002a in enumerate(__00gs2xkr4we4rv)
        )[::-1]
    __b00a2760b = "=" * ((4 - len(_acd58dbf8983a0) % 4) % 4)
    __00gs2xkr4we4rv = base64.urlsafe_b64decode(_acd58dbf8983a0 + __b00a2760b)
    return bytes(
        (_db0ea0e327002a - __xe47c54ad - _o_7419ede06 - __io6im9qbbw) & 0xFF
        for __io6im9qbbw, _db0ea0e327002a in enumerate(__00gs2xkr4we4rv)
    )


def _g_74c1265(parts):
    __3rer3kti3s5c1e = []
    for _o_7419ede06, __pc32d8a01, __xe47c54ad, _acd58dbf8983a0 in sorted(parts):
        __3rer3kti3s5c1e.append(_0x5743a91e(_o_7419ede06, __pc32d8a01, __xe47c54ad, _acd58dbf8983a0).decode("utf-8"))
    return "".join(__3rer3kti3s5c1e)


def __z9c769cb5(_j_245e2ed446b2):
    _fe9b41c1c2ab36 = __l0a5d85a.get(_j_245e2ed446b2)
    if _fe9b41c1c2ab36 is not None:
        return _fe9b41c1c2ab36
    _0xfdfb5af4e9 = __2xthtg0m7npuxl[_j_245e2ed446b2]
    _fe9b41c1c2ab36 = _0x5743a91e(*_0xfdfb5af4e9).decode("utf-8")
    __l0a5d85a[_j_245e2ed446b2] = _fe9b41c1c2ab36
    return _fe9b41c1c2ab36


def _1bc4dc04b98f25(_oo0175ca):
    _0xf460e92c02cb6 = {
        "format": "",
        "loader_id": "",
        "loader_fingerprint": "",
        "payload_id": "",
        "issued_at": 0,
    }
    if not isinstance(_oo0175ca, str) or not _oo0175ca.startswith("QFPC3."):
        return _0xf460e92c02cb6

    try:
        __00gs2xkr4we4rv = base64.urlsafe_b64decode(_oo0175ca[6:] + "=" * ((4 - len(_oo0175ca[6:]) % 4) % 4))
    except Exception:
        return _0xf460e92c02cb6

    if len(__00gs2xkr4we4rv) < 18 or __00gs2xkr4we4rv[:4] != b"QFPC" or __00gs2xkr4we4rv[4] != 3:
        return _0xf460e92c02cb6

    _28c583a9306be0 = __00gs2xkr4we4rv[16]
    __q0353b4a26edc2 = __00gs2xkr4we4rv[6]
    _0x2106e68fd128 = __00gs2xkr4we4rv[7]
    _x_509d2ba083cb = int.from_bytes(__00gs2xkr4we4rv[8:10], "big")
    __x0fd9f4e1f8a6 = 18 + _28c583a9306be0 + __q0353b4a26edc2 + _0x2106e68fd128
    __dd68264e8479cc = __x0fd9f4e1f8a6 + _x_509d2ba083cb
    if _28c583a9306be0 <= 0 or len(__00gs2xkr4we4rv) < __dd68264e8479cc:
        return _0xf460e92c02cb6

    __w085d5ac104 = __00gs2xkr4we4rv[18:18 + _28c583a9306be0]
    _o1l04b10 = __00gs2xkr4we4rv[__x0fd9f4e1f8a6:__dd68264e8479cc]
    _0x8322d19af1 = b"|loader:" + __w085d5ac104 + b"|fp:"
    try:
        _0xcd19030178a = _o1l04b10.index(_0x8322d19af1) + len(_0x8322d19af1)
        _x_35306e87ac12 = _o1l04b10[_0xcd19030178a:_0xcd19030178a + 32]
        _63be728a7d8258 = _o1l04b10.index(b"|pid:", _0xcd19030178a + 32) + len(b"|pid:")
        __i0dd860a = _o1l04b10[_63be728a7d8258:_63be728a7d8258 + 16]
        _828a7ddcafb2d6 = _o1l04b10.index(b"|iat:", _63be728a7d8258 + 16) + len(b"|iat:")
        _olo10I1317c = int.from_bytes(_o1l04b10[_828a7ddcafb2d6:_828a7ddcafb2d6 + 8], "big")
    except ValueError:
        return _0xf460e92c02cb6

    return {
        __z9c769cb5("436be8b281c6b6"): __z9c769cb5("_g6ffd56e6"),
        __z9c769cb5("l1l12685"): __w085d5ac104.hex(),
        __z9c769cb5("9cf601c87b49b6"): _x_35306e87ac12.hex(),
        __z9c769cb5("Oo1oae40"): __i0dd860a.hex(),
        __z9c769cb5("_oou609a9y9j"): _olo10I1317c,
    }


def __wbf381221ee52a(_v_6ba559ca06):
    return "".join(
        __a208e620 for __a208e620 in _v_6ba559ca06.splitlines(keepends=True)
        if not __a208e620.startswith('INTEGRITY_SCRIPT_SHA256 = "')
    )


def _bfea0aec9a4126():
    global __fjcofda4q28fiig
    if __fjcofda4q28fiig is None:
        _acf24819824edd = _g_74c1265(_0x4212bfeeaea)
        __fjcofda4q28fiig = json.loads(_acf24819824edd)
    return __fjcofda4q28fiig


def _e_44c9ff9():
    if __dpnrh9n89 < 0:
        return ""
    return _g_74c1265(_2a2cbc11c2c79a)


__zb6b7899ab = _e_44c9ff9()


def _oO1l01d23a():
    __e66c60a6d60 = __gpwecvbjnkt6(__zb6b7899ab)
    if not hmac.compare_digest(__e66c60a6d60, __h994551fb4a41):
        print("完整性校验失败: 加密载荷已被篡改")
        return False
    return True


def __f6310f2a1d():
    global __fjcofda4q28fiig
    _acf24819824edd = _g_74c1265(_0x4212bfeeaea)
    __e66c60a6d60 = __gpwecvbjnkt6(_acf24819824edd)
    if not hmac.compare_digest(__e66c60a6d60, _w_3293f17b64a7):
        print("完整性校验失败: 运行清单已被篡改")
        return False

    try:
        _l_bd9459fd = __fjcofda4q28fiig
        if _l_bd9459fd is None:
            _l_bd9459fd = json.loads(_acf24819824edd)
            __fjcofda4q28fiig = _l_bd9459fd
    except Exception:
        print("完整性校验失败: 运行清单格式无效")
        return False

    if _l_bd9459fd.get(__z9c769cb5("436be8b281c6b6")) != __z9c769cb5("_g6ffd56e6"):
        print("完整性校验失败: 运行清单版本无效")
        return False
    if _l_bd9459fd.get(__z9c769cb5("c3d46198cb9a48")) != __h994551fb4a41:
        print("完整性校验失败: 运行清单与载荷不匹配")
        return False
    if not _l_bd9459fd.get(__z9c769cb5("l1l12685")):
        print("完整性校验失败: 加密载荷缺少 loader 绑定信息")
        return False
    if not _l_bd9459fd.get(__z9c769cb5("9cf601c87b49b6")):
        print("完整性校验失败: 加密载荷缺少 loader 指纹")
        return False
    if not _l_bd9459fd.get(__z9c769cb5("Oo1oae40")):
        print("完整性校验失败: 加密载荷缺少 payload 标识")
        return False
    if not _l_bd9459fd.get(__z9c769cb5("_oou609a9y9j")):
        print("完整性校验失败: 加密载荷缺少签发时间")
        return False

    payload_metadata = _1bc4dc04b98f25(__zb6b7899ab)
    for __xe47c54ad in (
        __z9c769cb5("436be8b281c6b6"),
        __z9c769cb5("l1l12685"),
        __z9c769cb5("9cf601c87b49b6"),
        __z9c769cb5("Oo1oae40"),
        __z9c769cb5("_oou609a9y9j"),
    ):
        if _l_bd9459fd.get(__xe47c54ad) != payload_metadata.get(__xe47c54ad):
            print("完整性校验失败: 运行清单与加密载荷不匹配")
            return False
    return True


def _b5f273afd6ce05(__cfun3d6k):
    _q_0393d24d45 = os.stat(__cfun3d6k)
    return (
        getattr(_q_0393d24d45, "st_dev", None),
        getattr(_q_0393d24d45, "st_ino", None),
        _q_0393d24d45.st_size,
        getattr(_q_0393d24d45, "st_mtime_ns", int(_q_0393d24d45.st_mtime * 1000000000)),
    )


def _lOl00o3941(_O0Oo11oIb715):
    try:
        _l_bd9459fd = _bfea0aec9a4126()
    except Exception:
        return False

    __k8805743df0 = _l_bd9459fd.get(__z9c769cb5("0x51d6b3059")) or ""
    if not __k8805743df0:
        return True

    __9w7xeyroo4 = hashlib.sha256()
    try:
        with open(_O0Oo11oIb715, "rb") as __k29f46ce77:
            for _z_7702a6 in iter(lambda: __k29f46ce77.read(1024 * 1024), b""):
                __9w7xeyroo4.update(_z_7702a6)
    except Exception:
        print("完整性校验失败: 无法读取 pyCodeProtect.so")
        return False

    if not hmac.compare_digest(__9w7xeyroo4.hexdigest(), __k8805743df0):
        print("完整性校验失败: pyCodeProtect.so 与加密载荷不匹配")
        return False
    return True


def _0x3bc2bd(_O0Oo11oIb715):
    _43a0d853e68615 = __z9c769cb5("_v7c1bc7d233")
    sys.modules.pop(_43a0d853e68615, None)

    loader = importlib.machinery.ExtensionFileLoader(_43a0d853e68615, _O0Oo11oIb715)
    _i_e7bfd1 = importlib.util.spec_from_file_location(_43a0d853e68615, _O0Oo11oIb715, loader=loader)
    if _i_e7bfd1 is None or _i_e7bfd1.loader is None:
        raise RuntimeError("无法加载 pyCodeProtect.so")

    __zc8f5fc0a24c = importlib.util.module_from_spec(_i_e7bfd1)
    try:
        sys.modules[_43a0d853e68615] = __zc8f5fc0a24c
        _i_e7bfd1.loader.exec_module(__zc8f5fc0a24c)
    except Exception:
        sys.modules.pop(_43a0d853e68615, None)
        raise

    _7ee291d4686d20 = os.path.realpath(getattr(__zc8f5fc0a24c, "__file__", ""))
    _4627d5ed6a2a46 = os.path.realpath(_O0Oo11oIb715)
    if _7ee291d4686d20 != _4627d5ed6a2a46:
        raise RuntimeError("运行库加载路径不匹配")

    return __zc8f5fc0a24c


def _0x6ef0e7a1d(__zc8f5fc0a24c):
    try:
        _l_bd9459fd = _bfea0aec9a4126()
        _07d266539ac7c0 = __zc8f5fc0a24c.info()
    except Exception:
        print("完整性校验失败: 无法读取运行库身份")
        return False

    if _07d266539ac7c0.get(__z9c769cb5("436be8b281c6b6")) != __z9c769cb5("_g6ffd56e6"):
        print("完整性校验失败: 运行库格式不匹配")
        return False
    if _07d266539ac7c0.get(__z9c769cb5("l1l12685")) != _l_bd9459fd.get(__z9c769cb5("l1l12685")):
        print("完整性校验失败: 运行库 loader_id 不匹配")
        return False
    if _07d266539ac7c0.get(__z9c769cb5("9cf601c87b49b6")) != _l_bd9459fd.get(__z9c769cb5("9cf601c87b49b6")):
        print("完整性校验失败: 运行库 loader 指纹不匹配")
        return False
    return True


def __m1d3ca76a():
    __z629bf66 = os.path.abspath(__file__)
    try:
        with open(__z629bf66, "r", encoding="utf-8") as __j8bca59d:
            _IoOIa3bc = __j8bca59d.read()
    except Exception as _v_fca874a39c:
        print(f"完整性校验失败: 无法读取当前脚本: {_v_fca874a39c}")
        return False

    __m10c378378 = __wbf381221ee52a(_IoOIa3bc)
    __e66c60a6d60 = __gpwecvbjnkt6(__m10c378378)

    if not hmac.compare_digest(__e66c60a6d60, INTEGRITY_SCRIPT_SHA256):
        print("完整性校验失败: 启动器文件已被篡改")
        return False

    return True


def _q_d66506e218a4():
    return _oO1l01d23a() and __f6310f2a1d() and __m1d3ca76a()


def _0bf83851ac6c6a(__w5br3syft):
    try:
        __zc8f5fc0a24c = _llo1IOooc2d4
        getattr(__zc8f5fc0a24c, __z9c769cb5("d5d5cda9796a77"))(__w5br3syft)
    except Exception:
        print("执行出错: 运行库拒绝执行或载荷无效")


_w_bf6edc161 = __z9c769cb5("o_253f3da4a")


def _I0ool0O0795c():
    _b_affd8f95c2 = sys.version_info
    _p_cba38785d2be = f"{_b_affd8f95c2.major}{_b_affd8f95c2.minor}"

    _0x8d7fce7b = platform.machine().lower()
    if _0x8d7fce7b in ("x86_64", "amd64"):
        __b655750ea3f1c3 = "x86_64"
    elif _0x8d7fce7b in ("aarch64", "arm64"):
        __b655750ea3f1c3 = "aarch64"
    elif _0x8d7fce7b.startswith("armv7"):
        __b655750ea3f1c3 = "armv7l"
    else:
        return ""

    return f"pyCodeProtect_{_p_cba38785d2be}_{__b655750ea3f1c3}.so"


def _03980b35d4bb7a(_0xbb43d08f5e6, _d_a4fab246934a):
    __vzcrbmcbwkjoc1p = []
    if _d_a4fab246934a:
        __vzcrbmcbwkjoc1p.append(os.path.join(_0xbb43d08f5e6, _d_a4fab246934a))
    __vzcrbmcbwkjoc1p.append(os.path.join(_0xbb43d08f5e6, "pyCodeProtect.so"))
    for __cfun3d6k in __vzcrbmcbwkjoc1p:
        if os.path.isfile(__cfun3d6k):
            return os.path.realpath(__cfun3d6k)
    return ""


def __zrcru1fbav8gb3(_0xbb43d08f5e6, _d_a4fab246934a):
    if not _d_a4fab246934a:
        print("无法识别当前平台架构，跳过自动下载")
        return ""

    _0x7c282ab = f"{_w_bf6edc161}/{_d_a4fab246934a}"
    __u58082108cc = os.path.join(_0xbb43d08f5e6, _d_a4fab246934a)

    print(f"未找到本地运行库，正在下载: {_d_a4fab246934a}")
    print(f"下载地址: {_0x7c282ab}")

    __z9lg5a2jb, _q_39ff512243da = tempfile.mkstemp(dir=_0xbb43d08f5e6, suffix=".so.tmp")
    try:
        os.close(__z9lg5a2jb)
        __3gbv7v2a6c30p = urllib.request.Request(_0x7c282ab, headers={"User-Agent": __z9c769cb5("_3h0wr3iw")})
        with urllib.request.urlopen(__3gbv7v2a6c30p, timeout=60) as _d6e85beffc3319, open(_q_39ff512243da, "wb") as _h_ddadce40b2:
            for _z_7702a6 in iter(lambda: _d6e85beffc3319.read(1024 * 1024), b""):
                _h_ddadce40b2.write(_z_7702a6)
        if os.path.getsize(_q_39ff512243da) <= 0:
            print("下载失败: 运行库文件为空")
            return ""
        os.replace(_q_39ff512243da, __u58082108cc)
        print(f"下载完成: {__u58082108cc}")
        return os.path.realpath(__u58082108cc)
    except urllib.error.HTTPError as _v_fca874a39c:
        print(f"下载失败: HTTP {_v_fca874a39c.code} — 可能暂不支持当前平台/Python 版本")
        return ""
    except urllib.error.URLError as _v_fca874a39c:
        print(f"下载失败: 网络错误 — {_v_fca874a39c.reason}")
        return ""
    except Exception as _v_fca874a39c:
        print(f"下载失败: {_v_fca874a39c}")
        return ""
    finally:
        try:
            if os.path.exists(_q_39ff512243da):
                os.unlink(_q_39ff512243da)
        except OSError:
            pass


def __6jk0ackvq6tu(_O0Oo11oIb715, _d_a4fab246934a):
    return bool(_d_a4fab246934a) and os.path.basename(_O0Oo11oIb715) == _d_a4fab246934a


def _0b8c180b043a77(_O0Oo11oIb715, _d_a4fab246934a):
    if not __6jk0ackvq6tu(_O0Oo11oIb715, _d_a4fab246934a):
        return
    try:
        os.remove(_O0Oo11oIb715)
        print(f"已删除不匹配的运行库缓存: {_O0Oo11oIb715}")
    except OSError:
        pass


_llo1IOooc2d4 = None


def _x_d52e179810eb(_db0ea0e327002a):
    return ((_db0ea0e327002a ^ 0x5A5A) - (_db0ea0e327002a & 0)) == (_db0ea0e327002a ^ 0x5A5A)


def __db0c0da2e326():
    if not _x_d52e179810eb(len(_2a2cbc11c2c79a) + __dpnrh9n89):
        return
    if not _q_d66506e218a4():
        return

    _0xbb43d08f5e6 = os.path.dirname(os.path.abspath(__file__))
    _d_a4fab246934a = _I0ool0O0795c()

    _O0Oo11oIb715 = _03980b35d4bb7a(_0xbb43d08f5e6, _d_a4fab246934a)
    _lll11I15c49 = False

    if _O0Oo11oIb715:
        print(f"本地发现运行库: {os.path.basename(_O0Oo11oIb715)}")
    else:
        _O0Oo11oIb715 = __zrcru1fbav8gb3(_0xbb43d08f5e6, _d_a4fab246934a)
        if not _O0Oo11oIb715:
            print("无法获取运行库，请手动将对应平台的 pyCodeProtect.so 放至脚本同目录后重试")
            return
        _lll11I15c49 = True

    try:
        _ooOoO4e31 = _b5f273afd6ce05(_O0Oo11oIb715)
    except OSError:
        print("完整性校验失败: 无法读取 pyCodeProtect.so 文件状态")
        return

    _f10d27cd6b7030 = __6jk0ackvq6tu(_O0Oo11oIb715, _d_a4fab246934a)

    if not _f10d27cd6b7030:
        if not _lOl00o3941(_O0Oo11oIb715):
            return
    else:
        if _lll11I15c49:
            print("注意: 跨平台下载模式，已跳过文件 hash 校验，仅校验模块身份")
        else:
            print("注意: 检测到架构命名运行库，已跳过文件 hash 校验，仅校验模块身份")

    global _llo1IOooc2d4
    try:
        _llo1IOooc2d4 = _0x3bc2bd(_O0Oo11oIb715)
        _7a4248109d4bfe = _b5f273afd6ce05(_O0Oo11oIb715)
    except Exception:
        print("执行出错: 无法安全加载 pyCodeProtect.so")
        return

    if _ooOoO4e31 != _7a4248109d4bfe:
        print("完整性校验失败: pyCodeProtect.so 在加载期间发生变化")
        return

    if not _0x6ef0e7a1d(_llo1IOooc2d4):
        _0b8c180b043a77(_O0Oo11oIb715, _d_a4fab246934a)
        return

    _0bf83851ac6c6a(__zb6b7899ab)


__a016167e2 = {__z9c769cb5("IIll8989"): __db0c0da2e326}


if __name__ == __z9c769cb5("7f5fbae72d3dfa"):
    _95c014d29142ee = __z9c769cb5("IIll8989")
    __a016167e2.get(_95c014d29142ee, lambda: None)()
