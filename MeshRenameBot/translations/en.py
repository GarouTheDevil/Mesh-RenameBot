class EnTrans:
    
    WRONG_VALUE_ERROR = "**Invalid Value Entered For** {} **Variable**"
    
    START_MSG = "**Hello , I Am A Rename Bot**"
     
    CANCEL_MESSAGE = "**The Rename Has Been Canceled**"
    
    RENAME_NO_FILTER_MATCH = "**No Filter Matched Aborting Rename \nUsing The Filters To Rename As No Name Was Specified Manage Your Filters Using Cammand :** /filters"

    RENAME_FILTER_MATCH_USED = "**Using The Filters To Rename As No Name Was Specified Manage Your Filters Using** /filters"

    RENAME_NOFLTR_NONAME = "**Enter The Rename File Name In Format :** ```/rename NewFileName.format``` or ```Use /filters To Set Some Rename Filters```"

    RENAME_CANCEL = "**CANCEL**"

    RENAMING_FILE = "**Renaming ⏳**"
    
    DL_RENAMING_FILE = "**Downloading ⬇️**"

    RENAME_ERRORED_REPORT = "**Error Occurred**"

    RENAME_CANCEL_BY_USER = "**Canceled Successfully**"

    FLTR_ADD_LEFT_STR = "**Addition Filter :** <code>{}</code> <code> To Left</code>"
    FLTR_ADD_RIGHT_STR = "**Addition Filter :** <code>{}</code> <code> To Right</code>"
    FLTR_RM_STR = "**Remove Filter :*** <code>{}</code>"
    FLTR_REPLACE_STR = "**Replace Filter :** <code>{}</code> With <code>{}</code>"

    CURRENT_FLTRS = "**Filters :**"
    ADD_FLTR = "Add Filter"
    RM_FLTR = "Remove Filter"

    FILTERS_INTRO = """
</b>Filters :

• Replace Filter : This Filter Will Replace A
Given Word With The One You Specified
• Addition Filter : This Filter Will Add Given Word
At End Or Beginning
• Remove Filter : This Filter Will Remove Given Word From The While File Name</b>

"""

    ADD_REPLACE_FLTR = "Replace Filter"
    ADD_ADDITION_FLTR = "Addition Filter"
    ADD_REMOVE_FLTR = "Remove Filter"
    BACK = "BACK"

    REPALCE_FILTER_INIT_MSG = "Send The Message In This Format : <code>What To Replace | What To Replace With</code> \n/ignore To Go Back \nNote : Space After And Before '|' Will Be Considered"

    NO_INPUT_FROM_USER = "**No Input Received From You**"
    INPUT_IGNORE = "**Ignored Successfully**"
    WRONG_INPUT_FORMAT = "**The Input Is Not Valid , Check The Format Which Is Given**"
    REPLACE_FILTER_SUCCESS = "**Added The Replace Filter Successfully** <code>' {} '</code> **Will Be Replaced With** <code>' {} '</code>"

    ADDITION_FILTER_INIT_MSG = "**Enter The Text That You Want To Add Or Use Cammand :** /ignore **To Go Back**"

    ADDITION_FILTER_SUCCESS_LEFT = "**Added The Addition Filter Successfully** <code>{}</code> **Will Be Added To** <code>LEFT</code>"

    ADDITION_FILTER_SUCCESS_RIGHT = "**Added The Addition Filter Successfully** <code>{}</code> **Will Be Added To** <code>RIGHT</code>"

    ADDITION_LEFT = "Addition To LEFT"
    ADDITION_RIGHT = "Addition To RIGHT"

    ADDITION_POSITION_PROMPT = "**Where Do You Want To Add The Text**"

    REMOVE_FILTER_INIT_MSG = "**Enter The Text That You Want To Remove Or Use Cammand :** /ignore **To Go Back**"

    REMOVE_FILTER_SUCCESS = "**Added The Remove Filter Successfully** <code>{}</code> **Will Be Removed**"

    REPLY_TO_MEDIA = "**Reply** /rename **To A Media File**"

    HELP_STR = """
**Available Cammands :**

**•** /rename - **Reply To Media To Rename `/rename filename.extension` Or Use /rename For More With Filters
**•** /filters - **Add /Remove Filters Use this Cammad To See What Are These
**•** /setthumb - **Reply To Image To Set The Thumbnail Permanently
**•** /getthumb - **Get The Thumbnail Which Is Currently Set
**•** /clrthumb - **Remove The Thumbnail Which Is Set
**•** /mode - **To Change Upload Mode :**
           - Same Format As It Was Sent
           - Force to Document
           - Upload General Media
**•** /queue - **Gives The State Of Your Rename And The Load**
    """
