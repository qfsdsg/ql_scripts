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
Create at [2026-07-13 15:15:10 ]
Protect by 清风
"""
#   --------------------------------使用说明区--------------------------------
#   品赞 ipzan 自动登录并领取签到/钱包奖励，适配青龙面板。
#   
#   cron: 10 8 * * *
#   new Env('品赞签到');
#   
#   变量名：IPZAN_ACCOUNTS
#   格式：手机号#密码
#   多账号：使用 @ 分隔
#   示例：13800138000#password1@13900139000#password2
#   
#   通知：默认调用青龙 notify.py 发送通知，不需要额外配置通知开关变量。
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

_y_7287f2bf = 240
__jd97f91c24a314 = [
    (48, 1, 82, 'f4c8c0c4f9d8e6cff4f990cf90c5efc38498ced0f0abbeb0bffda28abc8d91ac9093b9b8da9c98b99cac4d795c3e615d7e616b36596d764a48770254777d4e74063d391d3b373713026451271f2c381d4a16170d0ff6d6ebd0d9a0be'),
    (62, 2, 109, 'JRUa5eD14uf2Fubs_Qv8_h4MAAI5OTgGNB0_DBA2HRkkGhwZNEcCCUZLPwcrPFItOlRAP1c2WxtXOC9eTk9AWDMgZzFgRjVRKldBYUlRb2w'),
    (37, 2, 42, 'sJecxcbEzMqguaeOv63TzpDWr7fZx6arvK3MwbGk16HF4L_go9nE1b3F6e6w1OXluLTOzvTyvLb3_vQC3ub83df-__gJBcbsDAP6EPXo99TM5_T29h0PGvsf4v35HRwC5xTeKArn6_r6LRs'),
    (13, 0, 165, 'd0c4fcf2e6c0d5d1d0e1c4fecbe08e85aaa4abbd8aa087fbbb88fd9ae3aab39e98b9f998bfbcea92bb99f1bf8d86d5d8d7a49793a993df9b81bc888cb1beaa9799caa2c285828dad90b5ca93a6ba6f496b3556'),
    (80, 1, 61, 'bad4eadae3e5c994f5e3fbdae2cce8f3c9f9b78ab3829de69ea0908da8aaa0bcbd86ba94aab1bc4f28257e565b77417277567114594a4675474b4f742f082a3b7b37150674191d2a2f220c583b33113f'),
    (52, 1, 223, '57796d4b575072196444035d790a4c331704082e3e08671c1c26002910331b042b113c4807f4c9fddcd9daf3a1d8d9ebc4cddffae1cb87c2f3ee88a1f18ef880b9a6eb84af80d491a286a2c491cbae346e6f7c5d4a2a66592e4b484d7d'),
    (64, 1, 156, 'beecad8fdfa5ac84a6a3aca5464973317d4b74616b6176106c65725e636653556a7c17150227033f0626050517562f2805294b26352807c6cdd8c5bbdca2dff4e5'),
    (66, 2, 249, 'prSTtaOzrbCkjHp8rIG9xIG9n5qgsYi-u86px73ExYyLyraSp8ypw7rVzqy9ucq_1MuhwrO2xOS37c4'),
    (96, 2, 116, 'QD0sOzIlKE8-KiIjUkwZVy0mXj0-QEFQMFNTVTweSls6WSw6Y2NTLzBBU2VJNGt3cVJpXVxfS3dtUIRHemRaSUFCXGhjgIJ8dZF9jFBzVXGLdliQn494ooSdl6JodXNneqWFkJ9qrIGRjoA'),
    (105, 1, 107, 'a7adb7a4bfa4b2aedbbe9e9da89284555542725973722e4a5b6a401447497a677e530e4f05162c086102676d30193c0e274a10253c351832254de4d4dce3f8e1a6c0a9e5ced9cbffe89dca'),
    (97, 0, 216, '4f026e5b0f5572792e352672003f34780f7a791f08201c6833352a1d033b6315090215281411372803525409345f130c3c235c01370c3c0a3e0132233d39101b0c3d2d3235064cccd8e8e7c0b3d2eee0bdb3bab4fccdedfca9e7e9f7cfc7fcffddc9f8d2ecf1f2cef7e6eaebe1d3f3e5c59d'),
    (129, 0, 5, 'c3becdd3cda6fcd5ecc2fee6e1dae4c7dbd3cbcea2c4f3d7d7f2e5c9d6c1f0f0f4c8fa9ae3f2c9fbcfc6e09cc3e3ebfafdda8cf3c3c8fed68aeef6a2a88dab978f84aba4bd8286aab4fc939e87bab58faeafa094b3b79b82bdbaae8fb1a2959f85d2be9ed993db9dc3ada2b791c5bfb2c192ba93b98dbd929b8e694a7a723760655f57665c6c67594046'),
    (139, 1, 183, '7513181b0b632d1a1f35180a540e3f2a3946334a29e0c7fdd3ffa6abc9eccbd89aceff999ee0e5f5ee90b4fb8ce4bbbcbc97e19ab9a58b869d879ab7bd8bb3cc723452665c6275586d6c4817'),
    (29, 1, 194, '9094d682dc8f9fa2aebb8b4770314b5f6a6b5e2c595453606f451f4a5f0456790a262e10261c626d323b2b352b0f0602153c242f1724effcd1a7cee6cbdfe3d5'),
    (85, 1, 72, 'd0e2cdceebd4fdfcffd68a87b082ae9e80e9e6e69a8e879492baa0bcc4adb2c8b0493b6071744b26615d7e7360525743195f604f55596b3a23397216082431032c2436363d593e3706020a13f3d2cde0eed2e4afd4c3c9e3f6cfdf83c3ee'),
    (87, 2, 12, 'vNGr3ZTfmte9oKLkt6LopOHm2rfl19z09M7tteX42ra4yOvVvsHX1eTg3r7-yPfx3uDi-sQK0vwN4gzsD_rw7xMPEBce-tz1DhkmEAQS3ugM_OrrGCLwAAMnNRUCFDITKfg2CQv1NDEWJkIPSS8hIh4MIClFSUw_'),
    (38, 2, 124, 'GPb-FhQU6trb7A0FIP4pJP_gHCABFu4sDxHwADAXEvguOj4cHQ4NHzc4PB0XBz8YGiQ3OEshN01LCw'),
    (71, 0, 185, '624d404629565e55615b3e3b4a416f3b5250764b5522255f53204354255c707959136a4e1d4950601d1d6f6d645e786e485404705773545b0d7b77425b584f0c6d31303a2037313e21250c0e357c2a201f64152000190407093510091b683c381250015629101c26505802201929230e121a013000131c1c0a482b020c2c1525fac4d4'),
    (100, 0, 173, '67792a4b5647567c5c554c74685d4e15606b7b147d7449594679404f75587c6a7057040c465e6771495e4e6d6b566505727111111f6b763b7929327d'),
    (116, 2, 84, 'OBAhEzY0NjkYQCcJSEwGECkjMQ40TTc5U1kaTi4YL0ovWD9XGT5XaEhpVls1XSpobSwvQ3RXM0RFVA'),
    (68, 1, 240, '7875497c2573151f051c073b6d3a142e350804402342214c0c4ff2cfdef2c4fbc2a6c3a5d3d2d5dd9edfd0faf9cafd9190989ca6babce1e09295b3d3d0bbdec686c5b5c55854497b457961506055475409614f5c67795a736c6c17297c323c631a156f6a0d20073959421c39554936b9c2b6dec8e3dcc3e8eff5cde9c7e4ebe48081d4eff2b092aba096ba92a2e2'),
    (2, 2, 150, '8g_HCO8N0-v0E_zz7wj_EPoR8iMjDgUA5iIsFRckJAfwJw4MKBwVAB_6EjEHOw4_OCIiHAIODxAREhlDKhYmCBA8DENEKkg0EjBTRShIGx9aNk8_UlBfIUBqPV8pKkhvMUwwbktpNmRrZENie0xPPmKCcHBlVHWHgUJlTGZ0XYhlRl1Q'),
    (73, 1, 43, '1f3c2c50caf6e4e5c3d6e1a1c8cfe9f9e1fde0e5fffbdbc9d1e9ae8d8ebb99e0879bebbfd09096b1b388a2c7b2b1ba4d6a3e6c60222b5c496d7947445a627a057c677f106d6e091b14163b3c602b2e131d053b40054547010513ddc9e5e9c6c6e6d2fefbe8fb'),
    (21, 0, 107, 'c5c0eacbdbd2e4e9d0c2dbbae1cee4dddff7a3dfa5d7d5dbe8faf7a8d3dff4e8ee9491c092939ee0c9f3e6e0c1e5cffdfcc8f8e2ffecfbc38ff6f5dcf5d2ee8b8c9885b7a68b898499a0fdb29b97aff9a4b7e7848d829181'),
    (14, 2, 17, 'gpROfIKSe2mLgm5ifoKlZXJyY3ljaW55kayba7GqdZWAc3mucK-nqXqJw4F8rZKdkZK-oZWJitCmi6LO'),
    (107, 1, 123, 'b2deaa859e988fd6ab7b346f7b395b4659517e2b1471407c4f60055808050c1b317c79072a621603682c2a3830382517011b2a29bab4'),
    (118, 1, 175, '4b51617c474e5c7e552a32747f35272013283e150b0f2108051f140f331f2df0bce1cfb6dfe4a3f5ec8dd3c8cae4e8d48dd0d4c9aaf080fd8084a6a78dea9b96d5da9b86849b8db8bf4c3b577f4f7b45785762776816437d7e5f655d506a0a361c3f0f202b0327340d181251031c073c20351c2af1f2c1e3dcddffd3f5d6d4'),
    (136, 1, 170, '476c680d77762c00057c681a7b1b0b681b57203a3c1f3323000ee2d3fcf0ddd8f9acb5c1f6f5def4fc9ddad1daf78aed91bdf1ad89b2e3e4889981ce838fb4bfc1acbba2ac6a5776336e7c7c44414f704974661c565b430475501a2e042c611b071309'),
    (40, 2, 53, 'r5aMkY7Vk8yvt6uump7S1cGe4Nq_wNXAwrvZ2eLkyuiqzsrQsuzM1Lrb2b3jugHF-N7f1QMB49vvEOft7erR7c_LFA8Z9gsGB_7dFiMbDxn0I_7nAigbIAMv'),
    (47, 0, 61, '5a00295f001d172c3c03300d361e4b4230150a2ce8c3dae5ebb4d7e8eef8c6e6dbcaeccbc2a0f5f1fdffccd4f9a0eeccd9ebdbfdda91eaededcbe2e899c5c7d3d89fe1dbd5f0c1f5ffeddddac8dcf8edef89dff0f59185fb89aa829d8c93ad8780b88facb2'),
    (31, 0, 124, 'aeccc5fdc093f4cdc9959c8bead2cd9de094ecd6ca89c985e381f9d2d6fee8d2cbfb84ebfdb3b197a18ab0ffa9bc9ca5a6b69d879aa4bfa2ea83e1e686918eade9ebe4b1908a8bbbb7bca4d7d3badcb0c6ad9ea49aa7879aa7a592cfa5a7ce'),
    (56, 0, 87, 'bcdba5aba7a2a1c9a3d0d3dcd5d9cffce8dafecad9dce0c5f8ffcddefd99eaccc7dcd2f4ecc0c7e2d9cfdacecef8f586e0b3f2a0998ef0f0f182ba8b85b8b4bf9be796a585a49ca5ee9ae180af8c8ce7f2b3ac9ad58286a39ea78da6a08883a4a6be8bb59cbc979a9fabc0ce8e9498b0cf726f4a565b6040433b5346433e5a684c4f78756a72747922404849595a'),
    (76, 2, 129, 'JB80KUksJQtIUCURUQpJET5ELDVHQUlcTk9PMkwzTR4gVGhBRkg-a11EPV49R0F0dmVnMDhRfHZ5XTo_UzqAfHhBUmpmg4BWe3d7Z0lramKE'),
    (7, 2, 235, 'J19TQWBWY2lnXT1KT0FhSFxlbj5nWWlPZFw_Zmdae3l1W2t6gW1NfkdLkHNkZFlVjZp4Wn2Ll5yfgXx1gnuogJ5ogZpjgX58f4d0tHWZk3Smjo24fJSnspijg5CmwJyFm5nEwKivxq-ov9LIxtiTzqy2pb_JydPi4g'),
    (5, 2, 15, 'hXhfX2NmUGqIamxPeHR6bJWXlG5bm6GWYKZ4mJKdX5plpqGrsKeAnGmStoOBqLWWrbG6kJWbn7CVpMO8oZ2nhcqjjqq_ndGoxNXKy9fE2Zzdr9G0sdzJpK2f4uXJ0-DgvLerpMrz'),
    (26, 0, 69, '282a315155172a245f092747325e1a373c32433a4a1e3f230f0b112a222a040431c3b3c6cad5bccdecffeed2e4e5daecd8f1e9c2a2e3fdf9d3dbf3c2edc3f7f5abe3f4ecfcefc6ef95faf6e8ed9cc9fdd5eae3d5c2'),
    (19, 2, 211, 'PUs6O01EJVNNTkVpOjZcQ2dKaGVdXyxAVGI2dzJabUdrV2JVZFo_Z3xGhUVoR11YfEh5YmZvcVJSYlBSZotnj22NYW2Ql2V8coZ2gGdog6CLp5qkpqpyiqCtuKWahLaOc5e1lY60r6XCl8KjyZSqjbmniLvJoau3v9bakqm0rJLSnNXCmrQ'),
    (130, 2, 45, '9vnj-yXqCxocLv0BIi4FAgwPBSzzF_oZERA2QkErLBABICc1HgcuRRgKKTlUDUhNFiZLKBoRKxZRVDo3G1lnXTY4REJV'),
    (39, 2, 16, 'aYaxcpWodJeWeZG1lbKreajBvcOtv7t_mJSTw7S7zcqikcadvrDHp7aXtbat1LeoyLusw6Kxt6TZseun39ys5-ngr8Pw0dzD49THtrvq_sv95wPtu-vsw-AE4vHKCA4LyeAFAA_NAQoZAc4OBPgRHvwa3g3tEQIP3Bk'),
    (16, 2, 111, '88ay2N3L1Lr16sDp1_LbvsLxC9nG5v_f7BHf6OHUBdYO8Nb0DtrY6eAi7t4X-QAWBvoJGQD3BQkwLyXzKB81JwswDPr2NCkHMT4-AUQEPAMDRhwxAyc0UCYjTgsSHihXETgyI0lHM1E0FUIyPEs-OzMyNkFAV0tAaEZeZ1pDc19GSkQ'),
    (28, 1, 91, '212838d7cac1e1d3e1c5f6eec4d6d6f2e2cec3e9dfc3f8cef2a991bcacf8e4e7a7afaf92d4b187a3ae969ba282924f7c683f5a3d72467a7570'),
    (141, 2, 53, '-AYxDhwqISEkNBE6FjIdKBgnSxwbUT4cHx8rJhc0KSVSSTRWRRxaPzA8YENQZyMpQF5pZF87Y01BP2JSbjBDNlJQU384SVR4S4F8Zj5UU4iMiGyLjHpQfmGHUJBRT1R7c5RWVXuanJqYeqGip2ZmlaeAaI-egqZvk6-Tl5GLj4WUhLeQ'),
    (86, 1, 15, '232d09074046332c37f3cbc7eee2c0e1ccebd8dfd4e7949d9ac9c6e1f4d68b91b5bc82ff84bbb9b2b1a8a880b0dcdfa7b3b9b2a173574867495649646c7379101169'),
    (20, 2, 8, 'lo-BVn9XlFpmeFh2kpmRmHSfoomVZ4CYeqt7gI-ibqyQgqSeqZSJknGdi358rn-2j7yyx8S2wIOnn8yazqDDstbEr8zOw6iVlNS_1Lm50J20psbl6tPox73X2e-57Q'),
    (131, 2, 68, '_jL6OhU8F0EEEhk3AEwgPEwROic8DygwWCxaMEpQN2AYSk4wHDI1WVBEHjRFaSojOWdIXg'),
    (78, 2, 56, '4LfT8NgFxMbn48fFB9gMxQML-wju6OcNBNbw7OXlGgsF6w7yAQQR-vMGJ_8f5OYs-OQN6h0BKQgmCfQbMyr29Q36DC4AM_7-LyJGOThF'),
    (102, 0, 119, '9b81988baca191b589d7908ed1bba09f81bd89b28087c5b7c3b39eaeaccab5b9b69c9c5162524054375262456658626e38615c53774763704441214a52685c7e4458796c644664541513417f1e13537f7f5655585f756b405f777857586541684d720a2203041722213f3203713d'),
    (95, 0, 213, '536f5b064a4349680f704a6514747a3a1b162a307124221928220a7d133d6b373e1935002912111a691618310212532b311c51140d180b252d255e0c17240618471b074f123b0b3d333c0408c2eaeecbfcf4c1ddccbec2cdc2d8dfb7fce9dfe1ada7a3c0a0d1edf0daa4f1fdf8c29196f4ccecff90ed9fefc1c2e09d85d0'),
    (42, 0, 77, '152a4b141415484b19facee4bae2cdbfc2fffdfccacbecd4a2f1d4d9feb9faccd5c9eaecd3cfd3d7e6ffd6c0cad0ca95fee1cefafbc2efe79ee0d0fac1e3c7c7fdcec1ce89feffd492aef9b68ca0b592a8a38293f389b5fa96e2a29995a6e5'),
    (22, 2, 53, 'e7y1sb-fo8m-waCthI6l0rDGla-4ja2xqK3XubbVu9q8rb-ip9G3ytvTvLzawc_N2vPO0sTu6K_L29r22rrY3df3BATbwQjK5Obf3w_9ywPvyQvV0BDoDAnyHxvr9hv24iMG_PIJ'),
    (1, 2, 123, 'zcDDx9W50tO8xsf_vN7f5d3eB8DC3sULCO7u4RL64eEP6fXtFvvp-dwI7hLe9iPfJPr2JyMT5PkfDw4A7gn7IQc0Ly4wAwkQ_RMSLDdB_RBAIAFHPTQWQgYWPx48STQiCVdIEVkqVjVUUT87NSFWRQ'),
    (99, 1, 142, 'b2bd83b2904879615b4460597d2e296a53127747666f51060f4574751d2c0036392527126851052c3a0d2208172b0846f9e6fee7f5f1d8f2fecaf2cdfdc29fcdd6e7faf5c590b4a087bdf9eaad95be9dd7b196878093c7bb9db48b3236647b4b576e7872454a505f105e026571094e5d73'),
    (90, 1, 222, '704e4c0c702d043f06120f0b25113a0c1f28194203302937b2ced2c8b5c3f8ded3ddd7dbddc587c0d9f8f388df86a7b4bdb1fb94e788af8b99d3b3b9998097bebece9a54655e6b7576416e506969'),
    (82, 2, 167, 'ZERSVmR1aVYzdlxmSmWAbnNAQnhkiHdIWVpidU58i2JokV-RcZZzj4JuWJKSWZOLmouYX3R3lpiBg3tsqXeokoOPr6t1pYmukqO2t7aUfol7ocOP'),
    (83, 1, 12, '3311070e245f0b2d354f2ac9aefffda1bec8b8edead4ced6e8fbe484e4e6d8d7cf86b2fda3fca7bc87e9ead7d2b5a4829e93b2abbeb371624e7a4e5d415552752e696071521e045d7b555028173f18220d3701'),
    (142, 1, 237, '240eb8e5c0e5bdcfe1f5fdaecdcad1fefee1dccec189cc8e8887999fa196b2e8b18dd3bbd293b99dbcce9ecece4a7f3c384b79255556504d75686e4f605c507f0b4c303e282d3f02271535'),
    (12, 2, 160, '4_4E4AYEKuAcJPsBAQrnIhEvKhDzIC0oNyYuHA0RGDtA_hgeMyApCUUMIT48BgorIk9HQTFINk1WNjw1Vx5hXSAgQSQ8Zzc9KVpEQkcua2l1aUxUdDlXV2loeTqBP1N8WFhtVFKBgA'),
    (36, 2, 3, 'mWp5XHmShYhcZWqVfaGDa2mibISBdbJ0kXOQhpeRqXp_qXp3t6-PoILAy6OivpqZxry7q6ywp6zOkZWttq3Tsw'),
    (44, 2, 204, 'UVNZQlFyS3gyblNtS25lenmBeEBNP2Nzin1niXdtSWyCgXGFYWh_bYdWZ3hrao5-bnB5oaOcc56Gdoecn6efhZeanqKRlHOHd7ersoezjKmse36gvpWzob-auJyboMnBj5K5uqWu'),
    (60, 0, 142, 'b999bbfcb7a694a094a9a6e2b09eb9b38ee8be84b28899848c8185d1a394a6a29b88a7b4ad8997c6abc0a19c9e8daca1b797cf849dac52533a35673257765173793a6b6848586652667d524f21752b735c7677717f4b134d41537d444a4d4b1a444d591e4c7a6a597b647656665276716d780a44660b197976153e0a2202107e0213071e7c26'),
    (55, 1, 123, 'defef3f0fcf8b3f1f2f9ba99bee98def86908c8cbe83c2b9c8847148656c744a546341722c5415774369767b000c664a1316182d270b2e396f130a2204051e593c40363a0acecdd7c0c5dcf7f7e1f0d692f3f298e5c9c3fef6dc8cb289fa99b98599bbacb8b6d3b2daa8b3c2be8dca9847'),
    (98, 2, 85, 'KPkrEhAs9S4UNzQ09Bs_HhUOOwIWPv5DADEz_wk7SUcIKydGDh9WEFAtOkNIGUspNRVMMUFSRlVSZzU3OlwiSD0pZUZhdUM3dTlYVDtxS2k0OVJkPHhYRld9el13amqMdlxcX49oiYZXc41bnXlsb2p_iA'),
    (128, 0, 132, '346461434445524a7a75487e6523685d39245746427759795b706d5e676e4e14164e505349611c476965586b56055a0a79447f73707f560e48544f07777835200b041122701b270a1a7e2738183d1111100f341c100603101e2c0d6f075404'),
    (34, 2, 6, 'jXd6ilxuhKd-ol-amWiGqKSAcXGos2uYcrGvnbK-sLq7e6yQlqCxu7iDmIrAnMK9hY6cz8K1ybHZxqvMkanFyKvPvZuf0NHhwNbK3aW7p6SvvMK89Mf43sjX77TW5tTdzQ'),
    (15, 2, 47, 'pJl2tJCurXi0vni0opSRkbmWxcfFnJ2fj6iOkdTIpcOUsJXDutva3MnQ1qrUys7cxNCn2sij3LznpMm6rbDbr8nUsLjM7vfKyrvT_uPB1_Hx1_r99e0CxeDj3_7t4g7mC_72F_UE5dk'),
    (9, 1, 117, '2cf4b5aaedfaa3c0a5e9f8fc90e9fbc8f9f5e48fd38982a6a48efb8393b1a89eecb8dc86bf8995a2bd9caf9c357f46456a477f522d78716b4c48017a76464b6b6b77751826743236051829330f1c38581a06444f280be6c7c5e5e0fed1f0dcd1fad6'),
    (91, 2, 135, 'Ei5NMi00IS1cM048J1MoaF4kPi1VaSgxM05UQC5eRWJ8UTVfcGZ_glhDhFRXPHmChVhobHx_bmplco-Sb2SEm2dWUW2db3h8YoR3haSUZXt8fKGHmKNwsIutspaNs7GgvIietpKxvY6B'),
    (133, 1, 121, 'bb4e776e5a205e5520605d4855574f12037675010b10362b710c0b08353f2e763a092f4a212006431b083d25d5f5ceeccadff2d3c3dfe8f4d484d5d8e0f78cc9d985ab8095a6a5e4b4b8e59989d489dd9baeb5b0'),
    (112, 2, 10, 'r-32v-_Drdvx_by6uMu1AwIE9t39_MEICAjt3PkQzwT-9fYA0RID8vT61-gYF_0f__kh4vMf4QPjHO354yz-DQguEiAGLfcW-Tg0EjT7QiMyNv0xEwQFFP8pPgIqPh5ELlNIRBMjOUUoKBRTVA'),
    (8, 0, 119, '4aedeaefd2c7c9ede9f9f1f2d9eec6cac9d4f6d0e1dab8dee6ebcdaac1f9d0adf5e7d8c5eff797efe2dbfec2fbc1f4c5cce8e9c4e9dad3f0d48dcd8ded8a85f3def8958ea1a588a1a89bfdf392febbbd8e8887a6bc8b8daf8f89a8978ee98ae993b4cca8b489bcd68ea7db92dcb3b5b1d69d9c99cbcc8da4a4b58fce8e9fadb58876644a6a50515e77'),
    (92, 0, 194, '502c786417715e164a467e7b1e1b466865176f7a4b017d7278557f0e600d0a440b0a272d340e77681626057e18283e0a77392a6011361b3d10340a0b3c0832056634242020093d233412212f293b552e035734032d43270c3c210d'),
    (67, 2, 253, 'r5S2pnGxqau4lqKBk7uVu4Ofq6m2ws-xisrDxJ3Sv6K5ztjbuJrcucLTy8_Qot6_6ruoyuDgx-alsuzI4dDM-A'),
    (27, 1, 159, 'f3e7ba94b3abbb9a97e39489938d8f8fbdb5a1b6a5beb99d6d6a3d454b6b526e6b6458411e1a49427878707171397331107c0f671231363854031b5825393c303f2bc2e7c0bafce1e3f0f9f2ebcbf496c0dad3fce3f6c8e586b5a2aeb7ba87e4'),
    (49, 1, 73, '2b2ff9e0b3d1b4d9fdf3fbb6dcdbd5c087e0f5f6fee3c4e6969286f28b9cadbfb8bf8491a9b6a18c9392b98fac36455f5f617b2160774d7c406a5b1b7e740c5e4c5c290a0c00187e04176976343e071119222f463335'),
    (74, 1, 13, '12361a25361720341c10224a0246b6c7c2ffc7f1d0a7afd2c5f5c398da9dc1e4e2ebcd959a89ff84f68591eab98f98d7a09dd9bb83bca8bad2414d593b5d62226d7758506f14764a4957716d61673820213e201f040215081426481e523c3d16330f12cbaefeecdee2f1fb'),
    (32, 1, 126, 'ff98f1ddcd94e9e1d0d2eddaafb1abb99babba8da284929081dfba958780b59c8e484858534258745d75705c1353401d46454704600e0d076b06783f07161b3d1137160c255925420e203433f5e6d2d2ffe5d9daadcad3f7f3c5c7ecc686ffeb'),
    (4, 0, 65, '377073787100091e1a2f3d3460072b67191d0333386f622f656a292c0c3401312e3914040a011a1b282929354830422d44140f3131001039394d2fc5e9cde6f6d0b4b6eecde1efe2d8bdfcd1d7bfa7dff9f1'),
    (122, 0, 25, 'f8fde5f1e7f0d5f6dcfaaffaebe1c7c7d9cfe397fec4f1f5dbf380d8e4c780dfe2def9d9ffdf8af4e2eec8c6f7949b89af8cb6ae8ba9ad8fa58597a482b7829ee58790'),
    (123, 2, 115, 'Vjc-VmFmWi0pWlxgQ2NAQkJgSGRZdHtccTRcX1N2UDpjWVt5QmJWdFeHkYqFXmd_coiDZItlVG5rhmmCgKA'),
    (110, 0, 17, '1bcce3cfc1fed2ecd1cab9e1dbd6e7e8bbe9d7c1f9e2dae5c3ddadabeceed5c7fbf9c3d492e9e093caebf0fed9cac39de8d3d2e78a8085e2d1dcd2d0ccfacb88879ab6978fb08e8abda0fb8daaffa096bcb296a6fe81bda3929bb68a968dabaaeecda7b2aa8cc8bf92af839eba'),
    (88, 0, 13, '3a2b10002a5c383b1e340e3a4313044c23413b3c0e381f251f4906c6b5c3d2cdccdcddc3cee7d1dbbac5bedfd2c8e7e5e4c3ffd6d6d8ffeed4f5c8c896f4f6f5fd93c5ebc2dbdcd4def7'),
    (79, 1, 151, '96b09997ca86beaaab4663586f35446a4f5d457a48541c181b446d6d54083a10090a02396a662c341130340b001722453e37334fefcbc7c7dcd6e2c6eb'),
    (3, 0, 113, '15063b360f35001d051e261cced5f2c0cbf6e7dff1c1b2bffaeec7ddcfe8e2c0dcc1fac0a1b4e8aff8f4faf2e7cbe5c6f4e0e3d7ffd0d3ec98d8c1dcc7c0e1eccc81c6c4d1ebe8cb91d9ec8e9093b48e92aff7b58b8395faa8a2be82'),
    (30, 0, 229, '546044684b597e734648427b3a7f64702524467579705b22282c65484a6d604e7777495571506748195f4048406543460a024660567f0d43417805786773773421141a0f2e01217d0a152b20150f292217201766332a1b3818063e671b2f572c5015293c5f22252c281b005a3749'),
    (124, 0, 60, 'eef797dd8dd3cbf2ed80a4b0b794b3eaa791f9fcbca494a883bfb8e1a2b49ee0bd95b1b38aa989ba99b7ac82bbd79fd5b78fa6bf9bafaa98c5938b9b9cc5c5ba90a9b8cf8b8aa6ba31603a374d73426e79685e7e747d44612143572275585c42762a285f51685d6b11456361'),
    (84, 0, 127, 'a2b197bb928791b3bebfb289998bb5a5bcb189ae8dad9f9b9cc1a1a39f8a99dfbbbcb9b29982bdcfaaab878cb36c39505233504b646c4747496d206d40625d7863444a5321762f57286e48'),
    (18, 0, 107, '25290ad2ebb5f9b3c2eae1c4c4c5f8efe4e5e5d8fff4e5e5dce3d8cbc6cbcdc6f8d1c6c8c0cdd1fd93d4c499df9ec4f3eb97eedefcd1c9ded7fd80d1fdd0f6fe8b86fe85b2b5a4f3b0b1b29290b28dbf88b798e0a1e7b9a48fb3b6acadaf9683ba'),
    (114, 2, 239, 'o8e9rpKW3q22up6ipK-7ncWj5OSs2MWo7c_n7r_z9bDO-e_6udjXvMz49vvS9Qjb1tT-Ce3v_gXazvQFCBXhAuIUF-rn3Qn8GiH65CUB5-kUHv8iJyYnKycOJjERMAo'),
    (46, 0, 8, '4355740b0b425b481365120a1d1605356b242a30332a0e28380d143f331d1e78073b6e323022686c1f0b4d05032d0e5d3933502d1d2c0b285f243f33181c163a1c401e0c57220424373aebd0e8b7b4a8f3d1b9bfdec5c5f8d4f6a4a2bfa5e5f8ffaea9dfd6ecadcdd2f8c2d295'),
    (72, 1, 11, '3164321d2c242c10391c4712062836c3ecf3badcfcd6e7a9aaced3eef29ad7c2c7eeddcbc594b4b8a5b9b5bfbeb0a7a3d5b4a6d8da9da590bdaa737e435e75767464435a5740137042435260'),
    (63, 0, 79, 'c9baa7d6a0c2fca5a6a2d3a0e0d1f9facdfdeacac596e2e2f2fd90c0f09cc0e1d69ddbe9c3ecd9d6dec7d0d4e2edd1f98ec7a3f990ee9489b6bf89bda99ca2a083abb696a49d8b8681be8b97a3ebae97ac9c84a7d4b1d1b3afd6df84dabb99aebc9da3bba49b8d82938782af8283908a8d9d4a4f476832746e66507e4f6521473a4e52287f4a5d707c'),
    (81, 2, 177, 'XDl8On0-f05rcYQ9gX-IYYVrZ4dfZ2VcblBmdYZTeWlrUF2aW1dtdnt5i5dfnqmpgIOEZpWAgm2LlW90saSWkK-rqKSSfX2ce8GwhpmehYOcwYrNoMCKw9Sdn42Ltay1zc2RvJjP4rQ'),
    (70, 0, 193, '513a653245397e3a77514426654560585b4960736a5a4827706a7b69567569634c1a1a465164587e584566595c06654505557e7d717e044f073609230d1b2c306a007a26317f1a79091939313c253626060c1b0f0e120f163d593813010e2a3c17215e0b2d58292125472e1a233e25021a2e0a0f0c151b4c13da'),
    (111, 0, 222, '1819282127161f106402301d292a21172f6c2c05512c363e34570b043d4758143e0c2d1a3830173833191d1f364b3728394e25e9b3f2b3b2e0d0f2e3d9ffdcbbfeebe6f5dea0c5f8dde7f2aaf4c8dcabdadacdd3c9da9494c294fdcc9bcbfffce0ff9a84dff0f1d8d7c684ecc8f88bdbfef0e0b384a6909b9cb7ab85fc95feb9b5f982a1bf93a7ec94ef92a29ea2ae'),
    (94, 2, 28, '06_o7ea37uL0vMzp1gHMA_7R9PMIxAXq_d7--BDq_-_O-vv_8e3Y0tr72w0UCvwN9QrjBQ_44P306R7q_xDqBusJKgnyMCX4DQ0jCz0RJ_0MDj0W-xxECkU8FTkJOzkdRlNWMlE3OENBLk4zODsdPlxQMFRAIVpXJitqJkk'),
    (59, 2, 117, 'GworDRf5ACgm6hQsIf4GKBf0Ei0m9jo-H_kiHxMmLzsnICYeRhYrIDwgPSsqP1ItIhUaPUo8Px4_LjMwRD5VNSZXVGMrO0ApXUk8bURkZ1hJTUhXeXl7aUl5VVJ4cDtjglNYjH1jgHloiWdnSZRRmWmXc5aJUnl9lF9soKaC'),
    (58, 2, 51, 'o6PapaOo0qvqzb3m5eX0zdfls8vO2M7Z-efR-u7D4_wH2vjm0uTeAvjq0AXMDf8T7OvrDgDtGe_aH98Q6_3d3iP3IB7nG_cB-Osw_Q4hEi8VMfgLOi0FCQ'),
    (132, 0, 64, 'f28b818887919dafabfea9bda282e7e7b7e1b1b69cbb90b2b18b89e883b383af8aa0d1b6ad8b87b287af9dbda19cc583969fc49bb1808dac97c8ac946334496b3257363751625a78654357417c574179465b6050'),
    (137, 0, 201, '05630c651726376a190d0b0e191712522e1602113c3459080529163a270d1d250426384007034a230d2a4e3e1030e9b0cae8fecac3f5eac5e5dadad2c8baddf3a4e4a4dbd3c8aaeed5f9e8a5ceadef96c1eacbe6ccebfdfc9ed3e6dc969cc5f2eddbd6d4dae7e8e9e2cbcfd4d7f3ba829bacf3af95aafcb898b38594a087'),
    (17, 2, 129, '6ebg6O3H8P3t3fIK0fn3FPTb9hMZHPgL-98THd8XJwYr-i4lHAoQJQYsKSoDBQcpNhIt9jYvQQ'),
    (113, 1, 74, '96e6f78397bc8ee4bb9195b48aadd7b8a98c9b9ddaceb663515339465b224f35795d73424d1a68097f5d5d481212280e32003403272a1f0d110a1059033531394309edd7cdc2dda0f7fcadcacffbcceb86e1f8fbfdd18ba48df68da3bc83bc9a8fb08eb5bd9fa4b6bb90b5'),
    (135, 0, 207, '2c07123e6b36093e6e6a56143d24515c0a0932273b5b26073b2c321f134b1e3e420d20413510492b1b48d6deb1c8e9f3beece6e2ecc5e9bae0c7fee2d8f0fca3fccfc8a8dea9acf1f6e799fbe8e993c8eff0cfd3ccc7e2d7dad6'),
    (54, 2, 216, 'ZoJaVVtLSI6LS3uKU2CLiYt4ZWJ8elaNlJqZbZWEkHJ_aHppaX6jdqZ8jrNytX-njHGPp7WMnYh6jqCZrXi_ua21lL6jyqG3qZ-ozLKeo8O90pPL0KXUtLyw2sHT09nS1brl5dPqzsXfue7Y0u7i1efQ6O_j89ff0urN'),
    (115, 2, 95, 'N005CAhRHlAkU1BCLy1LUylLVlM2Pj1cV2UyVzUyJWtIXjhLTHA6YEZkVmZ2Y1AuN0U6NllpazZybE49UFuBX2dIXUpohY1vgVNJTmh1ho53bZh4mZA'),
    (106, 1, 96, 'be9296e2958f9886ab80af9fdb809b9ec8c96f4b2b4f4f224556417a48724f491f1802600f684f770702302237093865191b190b34212257131b10392fe6ddf5edee'),
    (50, 2, 129, '5y4i7igmIy3tKvQlMxc0OxAmGzULABMLOx4kLRE7SCYASAwwIzAoSg9FPA4SUCtKKEgtMztWLU9DWVphPWlDP0xhIiYtTFwsTHI'),
    (6, 1, 129, 'c8ccfcc9f5f8c1aef8cbeefae9d8dcda80eadeb58596a3a1fab8e6eb82ead2d490ae80c798cfb0a5c82f4225796b5c7276426842691f605f4e474f57766c'),
    (23, 0, 58, '1537011123171f160d0e112d6d072d031107052311083139511d3d24205e59172241412330352e2f30393d2b4c193eeaf1b5b2e0c7cab3e0fcbacfc0fcdab6c1d7a1c1c5f6e6a0fcd8eff7f7edabddf3e0d4f6'),
    (108, 0, 217, '7c70051f263f7e1a14273826662124050212182f0e080e3a28132833152a2b343d1e211a3c53221d2357241e230435113a3c46213f001732242b1db3f0f2d1cbb6c0c6eacce6be'),
    (117, 1, 161, '254d4e54457c056d7b7973017055311c1221197d300c2f130624150f061a404538134436baf2f9c7bbe8c6d3d8aec5f0c8d8d8c3ddf9f689e6f49c868f81b6a991beb7f28389debf8f8998a4b78836377359355b714f285c744f660a6e4b084050084b55343217021d1961242b'),
    (125, 1, 205, '333f191803200e18503007532f1b2b222f33ebc1b4c1d4d9fdc4a1d1aecc94f6efeaf987f1e3d2cba59491a58cb09a9fb6ae85d2a2a8a0a2bccc9b82a65b69603a3f59505e5b6627401651'),
    (104, 0, 121, '9bb5a99e81838582d19f9dc1b8df8289a3949ca19c8c9d93b180b6c4a8ccbb50554b42464d4e4449605e5c3d57797e29567c7f6d413b24565377565f792b765472551441661f524f474b1b7c7279454a4807'),
    (120, 1, 231, '063120190d59223f361250dff2f7b9cfdfd9faecf5fcc7d09087e4c4f0ddf6fedeb5a2bca3a0e587efb29caea9b798ae85c69aad99ae6f6c736f60246b647c6a32106051721f735e7c690939340e113c2b7f3f353618245d550e1e1600461f3332c8b3ede4b9f5ecd5dcf5e3d4cdc581e1d0f68ecdf4aeb391a9'),
    (121, 0, 196, '0475797213752c21070a1f31181579253b361618081822223e35151e692f181d35042f39073b2a2f5c0a562a06023a211f251e09254a5e20370f3221211815121c0437b0f7babafcc6d7d1e1e1c0e5fffeffe0d2c1d3a1cca3dcdfd9ffa9aeaeb0e8e8f8efc1e4fdddf0ee9ccbee9d9c80c7dfe9e7e3e9f3e3e38ee789f6d5f6fa8ad2b0ec97a296909e928383baa6'),
    (0, 1, 208, 'bae1bf908a99cfb3aa91c3a5c2af90bf30714d5f6b3962566d496d51134b667c6f694600695015083b210b3b1f60092925501e0609233c4c353c3cf1ebf6fdc6f6d2c6d8ddddf3f4eddfe4f0f5d0d5fcb7828f8b81b88384828e8bcfd7a4baaba1'),
    (103, 1, 101, '9ef9a1b6a0bebcbb9795d3bf8196a18baa93356b705b23457b5b5c7c7411456258177d657616491213221d253e210f2d312b26003a5e273a42453b09d6b5b0f9d8bbaaa6ffe2c6f5f2e1e7fd8980f5dac5d98c89a6a8bc86859db6a4afb08bbeba9eb69a979db5706d613f7f547d474b7d696a724b4d7f645f4e6d6d2405732b613a2b131613082e'),
    (51, 2, 68, 'zuXax-rd3NbotfbF2bjq39fJy__RBffm_vbU2vnnAs_nCv7Qy90SBxgN6_rz-xoTFvIhGgEdFB4B--X3CggXIyDtHAESIvP3EC85C_sa9SgQDwpCMwA'),
    (143, 0, 150, '4d5c0a6d6b194156787c4152575d7505034f0e0d61657a7350577d0b7528197208710604000d3809253d26093b621e15203516221f3c3a1902086b37060d1513210a222c22091b412a1637181530402e423c1c4c1c2b2e3e163710efd5e6dcfef0'),
    (127, 2, 85, 'RCc4JzkbS0dWHzNNTTAsNDE5LFArLRtZXC8nXF8ePF5Abj5aXD1SQ2NnaTEtbzhZcXlrPDp3UFJNQFOFVT5bbE1dcHGNepSOdndLZJdUkZqenm5bh1yRnptadXiapItjeoWkarChk5yMjoqDjKKrq5x9nJysno-1nrG1qLy4tKa9noO2'),
    (75, 1, 241, '6552763419283b241a322b19252f55041d5b250c09123bf4f4e1e0faf8d7ecefa5acf3eddee5cd87e2cf8bdfa6abb2a1838db8b7b288958493'),
    (69, 0, 188, '3166554d554148667c49585f577a437d416b6558477f5641697c437d7b727542786f4455686b6a616f727a6d7c591d7c0062577e637362087d4e5678587b7e74372c373d71072b7f2019123a2a1836372962626c33621a68356b2f0e3517251630302e165d30093b06293d2f251929151a22183011'),
    (126, 0, 235, '3b0b0107061c1533172d3c300034150a4d2a2b28310426e1ebd3e4b7b1c0e3dec7b8dec6e3d4bcf8a6cdfccbe4c0ded6a1adacd8f0e4eff794eec5e3d3cfebe6cff0c79f9ae3fee389de8bdfc4d8f1e7caf6decb'),
    (140, 0, 5, 'c5d6d1d9c1f4a6d5cdd1e3ecffedddebc3efc9dc88f9e1fbc5d39adec3ccf6e9eee0e1d7faf483dbfafd8aedfac7c9988fa886a7ac81808d9c8ca3bff9949b88b28a849eb0ee9ebfbeee8385889490a388cfb3a7d6a9af8990b0b8bcbc85a7939bc7bfc0bab5ae90a997'),
    (138, 2, 117, 'WGNjb2x5PFxtV4NhWHhdfX6GcEVHaW16R1-BhWtdf1diVXaIiIlyVohfb3yMkYSkjppefoCCqYhpfZ6lfKqnh4eRhoN0hoqaqZ-KlqyxmcOStZ-enKmaz8S8rIfQoNbJyZDTlpa9mtTNtNXD1rzFpMidqdnqu6bczcyvrb_G8svg1tjy5Mve6ui8vQQ'),
    (33, 0, 243, '4474497d404f2950486a674e64504462656a47401d63446a58696f47620060724041795255767c6f49750f7209152375'),
    (57, 1, 183, 'b585accf968e31774e676a44677d4b677357117118777a56736a7b1b2520233c22246f150800175d12041a1f0e3b4e2db7c5ece6bae6ddd3d1fdce90eed7cbc2ead2c7e0dae08580b98f9e83bea493af93919e9b9cdbc2d88caca6706f527e7728'),
    (89, 0, 105, '8ab78ef0af8dac90fab986b98598a7a09b8abb829b98ba86ecb5ecb2bf9aad88db82a28dd791d8afba8cb4b99d87dd9e9ebf93c7a982cebc808b9f9bcb9b616e752e3d3d59625a5c434a4f6276597f595c2b46267474555c50506e6b266a4f705a72106a63716c7d59467a7f6a76415c7f5b707e5a0301'),
    (25, 2, 50, 'tX-EnLeVpIiAhs_NnKeOn5zSr6eguqTc2byzuci8sryi4KbPuKbb0cC9zsDCrs3qrfLVtvCyuLQ'),
    (11, 2, 90, 'q7fPqdCsrJ2dzdHS4Kjjt9_o5_DHx-HwtszD6Oftz9z28PzZ_wHPAeHn2__F-Abu6ene78nd9cwIBgYa'),
    (53, 1, 130, 'd6decaab96afa0ff96e386bcabbcabd7be93c0b88a87b89ea9553330595d26524469295a6c735d7656707b74707f1813747f071a2b1168376704215c3b2c433d162e48c1c8bfd3d8c6a6dfc8f2d0ece1dde6efe9f6'),
    (61, 2, 38, '0abKwJugorjSpN_Uu9Keo8faytDgzrvKyPPX8PK4w83Ivd727_C92eLP1c_z2NQDDcECC-npEejL0w0K6A'),
    (93, 2, 106, 'PPkMDP0xDjolIhU4QyFPGhpLHQ0NLhAWMBEWMjhPFz5aKzdjRFJbJD9hWWE5KzhwWWpEWXBURUV2eUNtO1xJTWFbXFpUhXheQoB3VV6NXYaIbICNYlJRXw'),
    (10, 1, 25, '1a1e5c7c5c58644c0e483932177a78666a232c2e07135d235b09482b133111caf7b0fcc0e6c3cdd7eeb3f0ddc1d0cffcebe2f3848f89f4a592a7a78e93b78d83d3d18fd5daa39988b6ba564c'),
    (65, 2, 87, 'CMoH9QDS9wUWFQX4-w7n3fwC_A3_2uIpJQLq_foiJw0x8isgEPEVI_UH7xAsED8XHfk_Iw'),
    (134, 1, 178, '097a6c067025053e0205231a1868503420190247420e380cc3e6fed8bdd5fedbd3d7f9f8cbc0d8c1e1e59be38ee58f92affe8aa3f9ee9096b1'),
    (109, 1, 130, '8787a1cda3b266413e785f406b41757740756a6b6d744540590e6a74757e792e361c651a212b323e210b2246230f08494fc8ceffedc0e4e7eff1f2'),
    (35, 1, 101, 'dfedc7e4e2e6ade9f6eaf3dbc9c4cbf1c8f3e180968f8bbeb5e69daf83ba8d9490ad86bc9fbd8fcb797b53487d43446c50704813655647495c55605a766623130b781e1c6011203a2a264b0641571818370b49dbbce3e5e0e0d0d2ececaaf8cfcee9e4c6d1c5ed8e8797aeac9d8de1bd8cb6efa3dda1dcd4c4a1bb9ea8ac306f655b3a'),
    (45, 0, 63, '2634201717340331011a1f35331f0d134b190832d1b7bbc1c5c6b2edb8dde9eda1e5fae8d1e5e1eadbf3a1d4acefd5dcd4eb'),
    (41, 2, 243, 'UGmTbHmEVZpubVh9baKNe5qfkKmjpn-srZqmmpFybICofpORg6iEi4V5h5d5w4y-mX-8fLeoorW8pJifyYauxqzJj5G_27bEl5u52brBxL3N46TOt8jH2t3Nt-fA0sCvrrDy6O_g_A'),
    (101, 2, 171, 'hltEiVxgWlyDTXN0lkpjUFmFWHB1ko5qd5qkjHiRnV97nWWtmouKb6mKroKhkZd0rbmsenu_m5mJjY60l5OUmaSBmoSruo7CjbPMx9a1tIzMk5ucsdGzvsm_48PWwt3BoNng5KrF6s7yqe7zxM6wytP60uXH9sjQAPvt-8_b9fnX2vE'),
    (43, 1, 251, '4b19736b717a406f44740c1d247a18113d6e133e1222263e0d2845061822d1e8f1bea1c6dddaa8c2fc94fef0ce9bcadadbe6f1f2ba8d829380939db5edee969a8cbda4a8b69faab1a9327d4e616a3d26414f4e294d6a1e194b535b6d6b4d0f05273d2b223b6c322f1d0f260527384605031f0c39caf1bfc3c6a2e3d1a8cae9c5f6c5e1d7d4e68acf'),
    (24, 1, 249, '6b447b7228677414665f4d6a41404a4d331c100d3d621f11086d09331623131e1f111a1f44e9b4b1efcdbdf0d0dfc8ebc0d5e19ac8e0e7e28c85f79ab089bfa29aed83bbbe85ad8ea0a1abc29fb0a99b3943334c7f477b4e4e454770494441435d715f'),
    (77, 2, 59, '2r261__55PfU-fHt-fvgzt3cx-32EM7i1BgS8Njc097_3B8lIfnz3-LiFPgjDAYrHSn_LTQ09Q0jBwcPBzD7Dg4P_S4DBUciGRYKGEE'),
    (144, 1, 240, 'cdcaeacac9d9f9a4f0f8f898d1d2c4f4c1c3c2f58df6f089b1aaaf80bfb3eaeb82a28ca2a2ddc0b7ba928f6860743d744546577c50557155634e6d67427978102e39272e2b2865200c69143b27313a043c3627'),
    (119, 1, 255, '39012d37fbbdbbbefcfcccc8abcfeacad2c0c3fee88df1f1d0b2a2beafa999bfa08d9ae880819280b495a19d8db9505c313c7840644a')
]
_e_2efc544 = [
    (5, 2, 152, 'A8DLwhEbFwwUFAYeDhweFRwc0erT5eHl5djj2isvKTAmKyQfNDEiNy0n-f3_7AXu70s'),
    (2, 1, 157, 'a890c4cbcf9882d6d69887e2a7af96a8aebdb9a1baaec3c8c588d994c1c7cecb9c3a643f693a'),
    (3, 1, 2, '276b693c722d712e7b4610161f484907070c085a78272179'),
    (1, 0, 24, '2d79787a2f2b2915184045411c1f15491e1319481e4f4b0902515203040e0f0108020f1e111c532f202626361a2f236a7368782f7d792c3132603235676f676c6f6968386e'),
    (0, 0, 127, '04a2e7edf1e9e4f2a5b2abdbcddccebdadbcb3fbe0e7e0f3f3c7f8eeb9a6aca9a79398979693959f8b8ac5c5cac8c8dcf0d6d8dcd4d1c7c6c5d1d7ce99869f8d89f0f3f0f2fda1a7f2f1f8a8aeafa8fdabb2e3e0e1b0e1e0eee1ece2'),
    (4, 1, 185, '8df9f5f2f1fff8b1edeabeeed18583d288c091c09bcd9e35673a6f382471262a7c461644484e4b53510e020878207479756263353d6d6f06525b0f594111425847a2b5b3bbede7e1cafcfaf1cdddc6da8f9c')
]
_lOII1Io48d5 = "d43a57d46e9bd322a65eb9abb6f7521148bbc24babd99ad6100a9c24f54f0c9b"
__xb78a03c5 = "5e07d37d01dc02833d9696dadbab5fa01e56d2b7a1b6b0e8da00e28c7384690f"
INTEGRITY_SCRIPT_SHA256 = "5be8a33848f8c2b3ce60deaae49c2b6540750b65e1c58d9b51d6e764b821ff0f"
__7om6vel073t = None
_IOIOO0o00a37 = {
    '_0sq06io6oqebo': (2475, 0, 222, 'e1fefffcfeb4a0bff6fbe7f1f0b8f4f7f4b5c9f3f2f5f6c58cd5c189f2ee88dbc6c7cef3d8ddcadcd4c1c0ebd3dfdbddca95c9ddca91d2a1b2b6a6b6eab5a8aea0a6ae'),
    'e70869fc5a64de': (3283, 0, 78, '515b604b4143775a465e4e4f59'),
    '_f4dj6m2fwv5py': (3749, 2, 57, 'UFRO'),
    '6ad9fcf48127d1': (597, 2, 34, '5_G86d_hzfDu9Obl97Hx5_z27PLw_ry_vcA'),
    '_j15f503a262d': (785, 0, 232, '9c948f8e84'),
    '_aob1zegi7': (39, 0, 233, '4f4e7f727d7b4948'),
    '_sprynwgyq': (788, 1, 64, '7a64190d2632'),
    'b_ca7260a': (2265, 0, 254, '869e8999e8'),
    'a_4311ed1': (2013, 0, 21, '949c86989783'),
    '31c76fcdee9acf': (910, 0, 251, 'f9ebf2e0e2efebcfe2faf2a6a0a0'),
    '_6ple5mearzjb': (891, 0, 182, '5d5d5250504468515d'),
    '0x4ed4bf39c3': (631, 2, 21, '-Pzv8_UD8fn9A_38CgkMBAoR'),
    '35217a60bd387e': (1808, 1, 108, '1816dde1e9e4e2e8f5e7'),
    'oIOI52b5': (2151, 2, 152, 'aHN0d2hoZGd7'),
    '_balnb42aup': (3327, 2, 41, 'mp6Yn5Wak46joJGmnJZobG4')
}
_0xc083bcf127d03 = {}


def _0x93c4bd3(_1b1c4eb029f84d):
    return hashlib.sha256(_1b1c4eb029f84d.encode("utf-8")).hexdigest()


def _o011ol218e(_i_8af6a5f49, _0x054c8fb7f, _s_d7beb7207, _0x66e4df):
    if _0x054c8fb7f == 0:
        _o10029cd = bytes.fromhex(_0x66e4df)
        return bytes(
            _1b1c4eb029f84d ^ ((_s_d7beb7207 + _i_8af6a5f49 + __a35hgwp0w) & 0xFF)
            for __a35hgwp0w, _1b1c4eb029f84d in enumerate(_o10029cd)
        )
    if _0x054c8fb7f == 1:
        _o10029cd = bytes.fromhex(_0x66e4df)
        return bytes(
            _1b1c4eb029f84d ^ ((_s_d7beb7207 + _i_8af6a5f49 + __a35hgwp0w * 3) & 0xFF)
            for __a35hgwp0w, _1b1c4eb029f84d in enumerate(_o10029cd)
        )[::-1]
    __tae68cac3b462f = "=" * ((4 - len(_0x66e4df) % 4) % 4)
    _o10029cd = base64.urlsafe_b64decode(_0x66e4df + __tae68cac3b462f)
    return bytes(
        (_1b1c4eb029f84d - _s_d7beb7207 - _i_8af6a5f49 - __a35hgwp0w) & 0xFF
        for __a35hgwp0w, _1b1c4eb029f84d in enumerate(_o10029cd)
    )


def __0m6mjrv1d7pa(parts):
    _OoOI9bb9 = []
    for _i_8af6a5f49, _0x054c8fb7f, _s_d7beb7207, _0x66e4df in sorted(parts):
        _OoOI9bb9.append(_o011ol218e(_i_8af6a5f49, _0x054c8fb7f, _s_d7beb7207, _0x66e4df).decode("utf-8"))
    return "".join(_OoOI9bb9)


def _j_86019e2ffe3fc(_0xfb53354b):
    _n_9b2767e = _0xc083bcf127d03.get(_0xfb53354b)
    if _n_9b2767e is not None:
        return _n_9b2767e
    _OO1OO0Of499 = _IOIOO0o00a37[_0xfb53354b]
    _n_9b2767e = _o011ol218e(*_OO1OO0Of499).decode("utf-8")
    _0xc083bcf127d03[_0xfb53354b] = _n_9b2767e
    return _n_9b2767e


def __c1c8c0bd(__ka8e5ca3):
    _q_f20aef4d101 = {
        "format": "",
        "loader_id": "",
        "loader_fingerprint": "",
        "payload_id": "",
        "issued_at": 0,
    }
    if not isinstance(__ka8e5ca3, str) or not __ka8e5ca3.startswith("QFPC3."):
        return _q_f20aef4d101

    try:
        _o10029cd = base64.urlsafe_b64decode(__ka8e5ca3[6:] + "=" * ((4 - len(__ka8e5ca3[6:]) % 4) % 4))
    except Exception:
        return _q_f20aef4d101

    if len(_o10029cd) < 18 or _o10029cd[:4] != b"QFPC" or _o10029cd[4] != 3:
        return _q_f20aef4d101

    _k_f30e47 = _o10029cd[16]
    __if4v5re6cs = _o10029cd[6]
    __x8b0bdc49a = _o10029cd[7]
    _Ol0oofee1 = int.from_bytes(_o10029cd[8:10], "big")
    _0x370463de136 = 18 + _k_f30e47 + __if4v5re6cs + __x8b0bdc49a
    __2bsrdgcs = _0x370463de136 + _Ol0oofee1
    if _k_f30e47 <= 0 or len(_o10029cd) < __2bsrdgcs:
        return _q_f20aef4d101

    _o1l0I1791 = _o10029cd[18:18 + _k_f30e47]
    _j_649c17 = _o10029cd[_0x370463de136:__2bsrdgcs]
    _0x1b48b826393 = b"|loader:" + _o1l0I1791 + b"|fp:"
    try:
        _a_1b5aedc6 = _j_649c17.index(_0x1b48b826393) + len(_0x1b48b826393)
        _ooIO108586 = _j_649c17[_a_1b5aedc6:_a_1b5aedc6 + 32]
        _x_6754f2 = _j_649c17.index(b"|pid:", _a_1b5aedc6 + 32) + len(b"|pid:")
        _6988ea40faf261 = _j_649c17[_x_6754f2:_x_6754f2 + 16]
        _33e9351ef8b4cd = _j_649c17.index(b"|iat:", _x_6754f2 + 16) + len(b"|iat:")
        _0xeb67a69b1 = int.from_bytes(_j_649c17[_33e9351ef8b4cd:_33e9351ef8b4cd + 8], "big")
    except ValueError:
        return _q_f20aef4d101

    return {
        _j_86019e2ffe3fc("a_4311ed1"): _j_86019e2ffe3fc("b_ca7260a"),
        _j_86019e2ffe3fc("_6ple5mearzjb"): _o1l0I1791.hex(),
        _j_86019e2ffe3fc("0x4ed4bf39c3"): _ooIO108586.hex(),
        _j_86019e2ffe3fc("35217a60bd387e"): _6988ea40faf261.hex(),
        _j_86019e2ffe3fc("oIOI52b5"): _0xeb67a69b1,
    }


def _Ioo0O2376(__f30d01d7f40):
    return "".join(
        _x_17e0895 for _x_17e0895 in __f30d01d7f40.splitlines(keepends=True)
        if not _x_17e0895.startswith('INTEGRITY_SCRIPT_SHA256 = "')
    )


def _0x2d7bbb6e2():
    global __7om6vel073t
    if __7om6vel073t is None:
        _i_8b49e9b120df = __0m6mjrv1d7pa(_e_2efc544)
        __7om6vel073t = json.loads(_i_8b49e9b120df)
    return __7om6vel073t


def _h_2c5eb8():
    if _y_7287f2bf < 0:
        return ""
    return __0m6mjrv1d7pa(__jd97f91c24a314)


__y03d9737efe740 = _h_2c5eb8()


def _f_6e1ceaf0():
    __y0l5664kfgxot = _0x93c4bd3(__y03d9737efe740)
    if not hmac.compare_digest(__y0l5664kfgxot, __xb78a03c5):
        print("完整性校验失败: 加密载荷已被篡改")
        return False
    return True


def _9a12e42a7fa02c():
    global __7om6vel073t
    _i_8b49e9b120df = __0m6mjrv1d7pa(_e_2efc544)
    __y0l5664kfgxot = _0x93c4bd3(_i_8b49e9b120df)
    if not hmac.compare_digest(__y0l5664kfgxot, _lOII1Io48d5):
        print("完整性校验失败: 运行清单已被篡改")
        return False

    try:
        _e4ff8280c2f8bb = __7om6vel073t
        if _e4ff8280c2f8bb is None:
            _e4ff8280c2f8bb = json.loads(_i_8b49e9b120df)
            __7om6vel073t = _e4ff8280c2f8bb
    except Exception:
        print("完整性校验失败: 运行清单格式无效")
        return False

    if _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("a_4311ed1")) != _j_86019e2ffe3fc("b_ca7260a"):
        print("完整性校验失败: 运行清单版本无效")
        return False
    if _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("31c76fcdee9acf")) != __xb78a03c5:
        print("完整性校验失败: 运行清单与载荷不匹配")
        return False
    if not _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("_6ple5mearzjb")):
        print("完整性校验失败: 加密载荷缺少 loader 绑定信息")
        return False
    if not _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("0x4ed4bf39c3")):
        print("完整性校验失败: 加密载荷缺少 loader 指纹")
        return False
    if not _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("35217a60bd387e")):
        print("完整性校验失败: 加密载荷缺少 payload 标识")
        return False
    if not _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("oIOI52b5")):
        print("完整性校验失败: 加密载荷缺少签发时间")
        return False

    payload_metadata = __c1c8c0bd(__y03d9737efe740)
    for _s_d7beb7207 in (
        _j_86019e2ffe3fc("a_4311ed1"),
        _j_86019e2ffe3fc("_6ple5mearzjb"),
        _j_86019e2ffe3fc("0x4ed4bf39c3"),
        _j_86019e2ffe3fc("35217a60bd387e"),
        _j_86019e2ffe3fc("oIOI52b5"),
    ):
        if _e4ff8280c2f8bb.get(_s_d7beb7207) != payload_metadata.get(_s_d7beb7207):
            print("完整性校验失败: 运行清单与加密载荷不匹配")
            return False
    return True


def _IOoo8cec(__j6c5ece):
    _0x7bc641ec = os.stat(__j6c5ece)
    return (
        getattr(_0x7bc641ec, "st_dev", None),
        getattr(_0x7bc641ec, "st_ino", None),
        _0x7bc641ec.st_size,
        getattr(_0x7bc641ec, "st_mtime_ns", int(_0x7bc641ec.st_mtime * 1000000000)),
    )


def __n28ec8b5c1bab(__lb3780ffa):
    try:
        _e4ff8280c2f8bb = _0x2d7bbb6e2()
    except Exception:
        return False

    __xn8e08b79iyl8n = _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("_balnb42aup")) or ""
    if not __xn8e08b79iyl8n:
        return True

    _226cc7570ae8c7 = hashlib.sha256()
    try:
        with open(__lb3780ffa, "rb") as __1j3wvji8:
            for __s4s6r7d2m4 in iter(lambda: __1j3wvji8.read(1024 * 1024), b""):
                _226cc7570ae8c7.update(__s4s6r7d2m4)
    except Exception:
        print("完整性校验失败: 无法读取 pyCodeProtect.so")
        return False

    if not hmac.compare_digest(_226cc7570ae8c7.hexdigest(), __xn8e08b79iyl8n):
        print("完整性校验失败: pyCodeProtect.so 与加密载荷不匹配")
        return False
    return True


def _g_ed83dd0(__lb3780ffa):
    _ca689ca9fa8b16 = _j_86019e2ffe3fc("e70869fc5a64de")
    sys.modules.pop(_ca689ca9fa8b16, None)

    loader = importlib.machinery.ExtensionFileLoader(_ca689ca9fa8b16, __lb3780ffa)
    _n_bb8659e17 = importlib.util.spec_from_file_location(_ca689ca9fa8b16, __lb3780ffa, loader=loader)
    if _n_bb8659e17 is None or _n_bb8659e17.loader is None:
        raise RuntimeError("无法加载 pyCodeProtect.so")

    __ja835d8396 = importlib.util.module_from_spec(_n_bb8659e17)
    try:
        sys.modules[_ca689ca9fa8b16] = __ja835d8396
        _n_bb8659e17.loader.exec_module(__ja835d8396)
    except Exception:
        sys.modules.pop(_ca689ca9fa8b16, None)
        raise

    _d_6b3091 = os.path.realpath(getattr(__ja835d8396, "__file__", ""))
    _0x079c27c65e9 = os.path.realpath(__lb3780ffa)
    if _d_6b3091 != _0x079c27c65e9:
        raise RuntimeError("运行库加载路径不匹配")

    return __ja835d8396


def _0xdc50e11ea(__ja835d8396):
    try:
        _e4ff8280c2f8bb = _0x2d7bbb6e2()
        __azmr0tkt = __ja835d8396.info()
    except Exception:
        print("完整性校验失败: 无法读取运行库身份")
        return False

    if __azmr0tkt.get(_j_86019e2ffe3fc("a_4311ed1")) != _j_86019e2ffe3fc("b_ca7260a"):
        print("完整性校验失败: 运行库格式不匹配")
        return False
    if __azmr0tkt.get(_j_86019e2ffe3fc("_6ple5mearzjb")) != _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("_6ple5mearzjb")):
        print("完整性校验失败: 运行库 loader_id 不匹配")
        return False
    if __azmr0tkt.get(_j_86019e2ffe3fc("0x4ed4bf39c3")) != _e4ff8280c2f8bb.get(_j_86019e2ffe3fc("0x4ed4bf39c3")):
        print("完整性校验失败: 运行库 loader 指纹不匹配")
        return False
    return True


def _l0OI1oOI5397():
    _0x517be1cfdfb7 = os.path.abspath(__file__)
    try:
        with open(_0x517be1cfdfb7, "r", encoding="utf-8") as _a571ee9991be92:
            __ivkbs3kz81j = _a571ee9991be92.read()
    except Exception as _fe3504989cbbb8:
        print(f"完整性校验失败: 无法读取当前脚本: {_fe3504989cbbb8}")
        return False

    __fy8e7f1pqrz3 = _Ioo0O2376(__ivkbs3kz81j)
    __y0l5664kfgxot = _0x93c4bd3(__fy8e7f1pqrz3)

    if not hmac.compare_digest(__y0l5664kfgxot, INTEGRITY_SCRIPT_SHA256):
        print("完整性校验失败: 启动器文件已被篡改")
        return False

    return True


def _0x072055b():
    return _f_6e1ceaf0() and _9a12e42a7fa02c() and _l0OI1oOI5397()


def _68d3a5a2513172(_I0IoI08c0a):
    try:
        __ja835d8396 = _u_f164847a8f32e
        getattr(__ja835d8396, _j_86019e2ffe3fc("_f4dj6m2fwv5py"))(_I0IoI08c0a)
    except Exception:
        print("执行出错: 运行库拒绝执行或载荷无效")


_h_d52f1b992 = _j_86019e2ffe3fc("_0sq06io6oqebo")


def _I011I11a861():
    _oo1o043e2 = sys.version_info
    _197b2b168e7d3f = f"{_oo1o043e2.major}{_oo1o043e2.minor}"

    __s693a48b0d48 = platform.machine().lower()
    if __s693a48b0d48 in ("x86_64", "amd64"):
        __t918c0b580 = "x86_64"
    elif __s693a48b0d48 in ("aarch64", "arm64"):
        __t918c0b580 = "aarch64"
    elif __s693a48b0d48.startswith("armv7"):
        __t918c0b580 = "armv7l"
    else:
        return ""

    return f"pyCodeProtect_{_197b2b168e7d3f}_{__t918c0b580}.so"


def _0xe665f2f1(_lIIII7368, _h_324ead9):
    _h_0645f8ab56b = []
    if _h_324ead9:
        _h_0645f8ab56b.append(os.path.join(_lIIII7368, _h_324ead9))
    _h_0645f8ab56b.append(os.path.join(_lIIII7368, "pyCodeProtect.so"))
    for __j6c5ece in _h_0645f8ab56b:
        if os.path.isfile(__j6c5ece):
            return os.path.realpath(__j6c5ece)
    return ""


def __d8628a585(_lIIII7368, _h_324ead9):
    if not _h_324ead9:
        print("无法识别当前平台架构，跳过自动下载")
        return ""

    _g_44e94de24 = f"{_h_d52f1b992}/{_h_324ead9}"
    _v_1b8532f446ea1 = os.path.join(_lIIII7368, _h_324ead9)

    print(f"未找到本地运行库，正在下载: {_h_324ead9}")
    print(f"下载地址: {_g_44e94de24}")

    _I0o01I13130, __kod1ac1mwd1w55 = tempfile.mkstemp(dir=_lIIII7368, suffix=".so.tmp")
    try:
        os.close(_I0o01I13130)
        _oOIIcd7b = urllib.request.Request(_g_44e94de24, headers={"User-Agent": _j_86019e2ffe3fc("6ad9fcf48127d1")})
        with urllib.request.urlopen(_oOIIcd7b, timeout=60) as _0xf1c22576e, open(__kod1ac1mwd1w55, "wb") as _IIOo003dd9:
            for __s4s6r7d2m4 in iter(lambda: _0xf1c22576e.read(1024 * 1024), b""):
                _IIOo003dd9.write(__s4s6r7d2m4)
        if os.path.getsize(__kod1ac1mwd1w55) <= 0:
            print("下载失败: 运行库文件为空")
            return ""
        os.replace(__kod1ac1mwd1w55, _v_1b8532f446ea1)
        print(f"下载完成: {_v_1b8532f446ea1}")
        return os.path.realpath(_v_1b8532f446ea1)
    except urllib.error.HTTPError as _fe3504989cbbb8:
        print(f"下载失败: HTTP {_fe3504989cbbb8.code} — 可能暂不支持当前平台/Python 版本")
        return ""
    except urllib.error.URLError as _fe3504989cbbb8:
        print(f"下载失败: 网络错误 — {_fe3504989cbbb8.reason}")
        return ""
    except Exception as _fe3504989cbbb8:
        print(f"下载失败: {_fe3504989cbbb8}")
        return ""
    finally:
        try:
            if os.path.exists(__kod1ac1mwd1w55):
                os.unlink(__kod1ac1mwd1w55)
        except OSError:
            pass


def _u_8c9a2a6185a1f(__lb3780ffa, _h_324ead9):
    return bool(_h_324ead9) and os.path.basename(__lb3780ffa) == _h_324ead9


def _Ol0006803(__lb3780ffa, _h_324ead9):
    if not _u_8c9a2a6185a1f(__lb3780ffa, _h_324ead9):
        return
    try:
        os.remove(__lb3780ffa)
        print(f"已删除不匹配的运行库缓存: {__lb3780ffa}")
    except OSError:
        pass


_u_f164847a8f32e = None


def _oIo0lo1e7ee(_1b1c4eb029f84d):
    return ((_1b1c4eb029f84d ^ 0x5A5A) - (_1b1c4eb029f84d & 0)) == (_1b1c4eb029f84d ^ 0x5A5A)


def _w_71649647fe():
    if not _oIo0lo1e7ee(len(__jd97f91c24a314) + _y_7287f2bf):
        return
    if not _0x072055b():
        return

    _lIIII7368 = os.path.dirname(os.path.abspath(__file__))
    _h_324ead9 = _I011I11a861()

    __lb3780ffa = _0xe665f2f1(_lIIII7368, _h_324ead9)
    __k5b55368d = False

    if __lb3780ffa:
        print(f"本地发现运行库: {os.path.basename(__lb3780ffa)}")
    else:
        __lb3780ffa = __d8628a585(_lIIII7368, _h_324ead9)
        if not __lb3780ffa:
            print("无法获取运行库，请手动将对应平台的 pyCodeProtect.so 放至脚本同目录后重试")
            return
        __k5b55368d = True

    try:
        __l1b84b4f179 = _IOoo8cec(__lb3780ffa)
    except OSError:
        print("完整性校验失败: 无法读取 pyCodeProtect.so 文件状态")
        return

    _d_c45fc272c651 = _u_8c9a2a6185a1f(__lb3780ffa, _h_324ead9)

    if not _d_c45fc272c651:
        if not __n28ec8b5c1bab(__lb3780ffa):
            return
    else:
        if __k5b55368d:
            print("注意: 跨平台下载模式，已跳过文件 hash 校验，仅校验模块身份")
        else:
            print("注意: 检测到架构命名运行库，已跳过文件 hash 校验，仅校验模块身份")

    global _u_f164847a8f32e
    try:
        _u_f164847a8f32e = _g_ed83dd0(__lb3780ffa)
        __gxaexlotqtl2odr = _IOoo8cec(__lb3780ffa)
    except Exception:
        print("执行出错: 无法安全加载 pyCodeProtect.so")
        return

    if __l1b84b4f179 != __gxaexlotqtl2odr:
        print("完整性校验失败: pyCodeProtect.so 在加载期间发生变化")
        return

    if not _0xdc50e11ea(_u_f164847a8f32e):
        _Ol0006803(__lb3780ffa, _h_324ead9)
        return

    _68d3a5a2513172(__y03d9737efe740)


__se1ed39c3 = {_j_86019e2ffe3fc("_j15f503a262d"): _w_71649647fe}


if __name__ == _j_86019e2ffe3fc("_aob1zegi7"):
    __qdb8de94 = _j_86019e2ffe3fc("_j15f503a262d")
    __se1ed39c3.get(__qdb8de94, lambda: None)()
