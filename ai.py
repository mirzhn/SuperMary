from config import API_GROQ
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage

class Summarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "llama-3.1-8b-instant"

        # Инициализируем persistent_prompt
        self.persistent_prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a helpful assistant that summarizes conversations."),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}")
        ])

    # Подаем на вход историю чата Telegram в формате JSON и промпт-запрос к LLM
    def summarize(self, text_to_summarize, summarization_prompt):
        llm = ChatGroq(api_key=self.api_key, model=self.model )
        # Здесь будем хранить историю запросов/промптов
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        chat_llm_chain = LLMChain(
            llm=llm,
            prompt=self.persistent_prompt,
            verbose=False,
            memory=memory,
        )
        init_prompt = summarization_prompt.format(text_to_summarize=text_to_summarize)
        return chat_llm_chain.predict(human_input=init_prompt), chat_llm_chain
    

# Создаем экземпляр Summarizer
summarizer = Summarizer(API_GROQ)

# Пример текста для обобщения
text_to_summarize = """
{
 "name": "рабочий чат",
 "type": "private_supergroup",
 "id": 1787463754,
 "messages": [
  {
   "id": 48166,
   "type": "message",
   "date": "2024-08-22T09:14:46",
   "date_unixtime": "1724307286",
   "from": "Миша Герман",
   "from_id": "user312947484",
   "reply_to_message_id": 48163,
   "text": "о, помню с ними коллаб был)",
   "text_entities": [
    {
     "type": "plain",
     "text": "о, помню с ними коллаб был)"
    }
   ]
  },
  {
   "id": 48167,
   "type": "message",
   "date": "2024-08-22T09:15:07",
   "date_unixtime": "1724307307",
   "from": "Миша Герман",
   "from_id": "user312947484",
   "reply_to_message_id": 48164,
   "text": "у тебя впн России что ли?)",
   "text_entities": [
    {
     "type": "plain",
     "text": "у тебя впн России что ли?)"
    }
   ]
  },
  {
   "id": 48168,
   "type": "message",
   "date": "2024-08-22T09:15:22",
   "date_unixtime": "1724307322",
   "edited": "2024-08-22T09:15:30",
   "edited_unixtime": "1724307330",
   "from": "Миша Герман",
   "from_id": "user312947484",
   "reply_to_message_id": 48164,
   "text": "сслку дай, проверим, не замечал",
   "text_entities": [
    {
     "type": "plain",
     "text": "сслку дай, проверим, не замечал"
    }
   ]
  },
  {
   "id": 48169,
   "type": "message",
   "date": "2024-08-22T23:30:16",
   "date_unixtime": "1724358616",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "text": [
    {
     "type": "link",
     "text": "https://vm.tiktok.com/ZGe3CDvx2/"
    }
   ],
   "text_entities": [
    {
     "type": "link",
     "text": "https://vm.tiktok.com/ZGe3CDvx2/"
    }
   ]
  },
  {
   "id": 48170,
   "type": "message",
   "date": "2024-08-22T23:39:03",
   "date_unixtime": "1724359143",
   "edited": "2024-08-22T23:39:09",
   "edited_unixtime": "1724359149",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48169,
   "text": "господи, первый раз открылось что-то без установки",
   "text_entities": [
    {
     "type": "plain",
     "text": "господи, первый раз открылось что-то без установки"
    }
   ]
  },
  {
   "id": 48171,
   "type": "message",
   "date": "2024-08-22T23:39:09",
   "date_unixtime": "1724359149",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "больше этому обрадовался",
   "text_entities": [
    {
     "type": "plain",
     "text": "больше этому обрадовался"
    }
   ]
  },
  {
   "id": 48172,
   "type": "message",
   "date": "2024-08-22T23:39:15",
   "date_unixtime": "1724359155",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "прости",
   "text_entities": [
    {
     "type": "plain",
     "text": "прости"
    }
   ]
  },
  {
   "id": 48173,
   "type": "message",
   "date": "2024-08-22T23:39:20",
   "date_unixtime": "1724359160",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "text": "Го спортс",
   "text_entities": [
    {
     "type": "plain",
     "text": "Го спортс"
    }
   ]
  },
  {
   "id": 48174,
   "type": "message",
   "date": "2024-08-22T23:39:28",
   "date_unixtime": "1724359168",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "го",
   "text_entities": [
    {
     "type": "plain",
     "text": "го"
    }
   ]
  },
  {
   "id": 48175,
   "type": "message",
   "date": "2024-08-23T08:06:15",
   "date_unixtime": "1724389575",
   "edited": "2024-08-23T08:16:53",
   "edited_unixtime": "1724390213",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "photo": "(File not included. Change data exporting settings to download.)",
   "width": 968,
   "height": 1280,
   "text": "",
   "text_entities": []
  },
  {
   "id": 48176,
   "type": "message",
   "date": "2024-08-23T08:08:42",
   "date_unixtime": "1724389722",
   "edited": "2024-08-23T08:08:53",
   "edited_unixtime": "1724389733",
   "from": "Илья",
   "from_id": "user418093361",
   "forwarded_from": "Кипр. Коротко и по делу.",
   "text": "В пятницу на Кипре ожидается некоторая передышка от жары: в горах и, возможно, в глубине страны пройдут отдельные дожди.",
   "text_entities": [
    {
     "type": "plain",
     "text": "В пятницу на Кипре ожидается некоторая передышка от жары: в горах и, возможно, в глубине страны пройдут отдельные дожди."
    }
   ]
  },
  {
   "id": 48177,
   "type": "message",
   "date": "2024-08-23T08:08:57",
   "date_unixtime": "1724389737",
   "edited": "2024-08-23T08:09:05",
   "edited_unixtime": "1724389745",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "отдыхайте глупцы",
   "text_entities": [
    {
     "type": "plain",
     "text": "отдыхайте глупцы"
    }
   ]
  },
  {
   "id": 48178,
   "type": "message",
   "date": "2024-08-23T08:09:02",
   "date_unixtime": "1724389742",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "reply_to_message_id": 48176,
   "text": "каеф",
   "text_entities": [
    {
     "type": "plain",
     "text": "каеф"
    }
   ]
  },
  {
   "id": 48179,
   "type": "message",
   "date": "2024-08-23T08:09:12",
   "date_unixtime": "1724389752",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "text": "сегодня даже облачка в небе есть)",
   "text_entities": [
    {
     "type": "plain",
     "text": "сегодня даже облачка в небе есть)"
    }
   ]
  },
  {
   "id": 48180,
   "type": "message",
   "date": "2024-08-23T10:09:42",
   "date_unixtime": "1724396982",
   "edited": "2024-08-23T10:10:10",
   "edited_unixtime": "1724397010",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "миша только что сравнил библию с майнкампфом",
   "text_entities": [
    {
     "type": "plain",
     "text": "миша только что сравнил библию с майнкампфом"
    }
   ]
  },
  {
   "id": 48181,
   "type": "message",
   "date": "2024-08-23T10:09:50",
   "date_unixtime": "1724396990",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "просто чтобы вы знали",
   "text_entities": [
    {
     "type": "plain",
     "text": "просто чтобы вы знали"
    }
   ]
  },
  {
   "id": 48182,
   "type": "message",
   "date": "2024-08-23T10:10:15",
   "date_unixtime": "1724397015",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "text": "причем не в пользу библии",
   "text_entities": [
    {
     "type": "plain",
     "text": "причем не в пользу библии"
    }
   ]
  },
  {
   "id": 48183,
   "type": "message",
   "date": "2024-08-23T10:25:02",
   "date_unixtime": "1724397902",
   "edited": "2024-08-23T10:25:21",
   "edited_unixtime": "1724397921",
   "from": "Миша Герман",
   "from_id": "user312947484",
   "text": "мысль была что обе книги имеют историческую ценность",
   "text_entities": [
    {
     "type": "plain",
     "text": "мысль была что обе книги имеют историческую ценность"
    }
   ]
  },
  {
   "id": 48184,
   "type": "message",
   "date": "2024-08-23T10:25:25",
   "date_unixtime": "1724397925",
   "from": "Миша Герман",
   "from_id": "user312947484",
   "text": "ой всё",
   "text_entities": [
    {
     "type": "plain",
     "text": "ой всё"
    }
   ]
  },
  {
   "id": 48185,
   "type": "message",
   "date": "2024-08-23T19:19:57",
   "date_unixtime": "1724429997",
   "edited": "2024-08-23T19:20:21",
   "edited_unixtime": "1724430021",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "photo": "(File not included. Change data exporting settings to download.)",
   "width": 1080,
   "height": 984,
   "text": "",
   "text_entities": []
  },
  {
   "id": 48186,
   "type": "message",
   "date": "2024-08-23T20:36:56",
   "date_unixtime": "1724434616",
   "from": "Илья",
   "from_id": "user418093361",
   "text": [
    {
     "type": "hashtag",
     "text": "#каламбуры"
    },
    " \n\nКак называются маленькие деньги, которые очень сильно боятся?"
   ],
   "text_entities": [
    {
     "type": "hashtag",
     "text": "#каламбуры"
    },
    {
     "type": "plain",
     "text": " \n\nКак называются маленькие деньги, которые очень сильно боятся?"
    }
   ]
  },
  {
   "id": 48187,
   "type": "message",
   "date": "2024-08-23T20:38:41",
   "date_unixtime": "1724434721",
   "from": "Илья",
   "from_id": "user418093361",
   "text": [
    {
     "type": "mention",
     "text": "@Furygale"
    },
    " ",
    {
     "type": "mention",
     "text": "@germanmixa"
    },
    " ",
    {
     "type": "mention",
     "text": "@mirzhn"
    },
    " ",
    {
     "type": "mention",
     "text": "@meantrust"
    },
    " ",
    {
     "type": "mention",
     "text": "@yamamotoshockers"
    }
   ],
   "text_entities": [
    {
     "type": "mention",
     "text": "@Furygale"
    },
    {
     "type": "plain",
     "text": " "
    },
    {
     "type": "mention",
     "text": "@germanmixa"
    },
    {
     "type": "plain",
     "text": " "
    },
    {
     "type": "mention",
     "text": "@mirzhn"
    },
    {
     "type": "plain",
     "text": " "
    },
    {
     "type": "mention",
     "text": "@meantrust"
    },
    {
     "type": "plain",
     "text": " "
    },
    {
     "type": "mention",
     "text": "@yamamotoshockers"
    }
   ]
  },
  {
   "id": 48188,
   "type": "message",
   "date": "2024-08-23T20:38:59",
   "date_unixtime": "1724434739",
   "edited": "2024-08-23T20:39:06",
   "edited_unixtime": "1724434746",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "text": "Видел",
   "text_entities": [
    {
     "type": "plain",
     "text": "Видел"
    }
   ]
  },
  {
   "id": 48189,
   "type": "message",
   "date": "2024-08-23T20:39:43",
   "date_unixtime": "1724434783",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "когда украл бэху, приезжаешь на район, а там уже есть такая",
   "text_entities": [
    {
     "type": "plain",
     "text": "когда украл бэху, приезжаешь на район, а там уже есть такая"
    }
   ]
  },
  {
   "id": 48190,
   "type": "message",
   "date": "2024-08-23T20:41:00",
   "date_unixtime": "1724434860",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "reply_to_message_id": 48186,
   "text": "Пугаксики?",
   "text_entities": [
    {
     "type": "plain",
     "text": "Пугаксики?"
    }
   ]
  },
  {
   "id": 48191,
   "type": "message",
   "date": "2024-08-23T20:41:21",
   "date_unixtime": "1724434881",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48190,
   "text": "мимо",
   "text_entities": [
    {
     "type": "plain",
     "text": "мимо"
    }
   ]
  },
  {
   "id": 48192,
   "type": "message",
   "date": "2024-08-23T20:41:23",
   "date_unixtime": "1724434883",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "reply_to_message_id": 48189,
   "text": "Бэхзец",
   "text_entities": [
    {
     "type": "plain",
     "text": "Бэхзец"
    }
   ]
  },
  {
   "id": 48193,
   "type": "message",
   "date": "2024-08-23T20:41:33",
   "date_unixtime": "1724434893",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "reply_to_message_id": 48189,
   "text": "Это тоже Каламбур?",
   "text_entities": [
    {
     "type": "plain",
     "text": "Это тоже Каламбур?"
    }
   ]
  },
  {
   "id": 48194,
   "type": "message",
   "date": "2024-08-23T20:41:56",
   "date_unixtime": "1724434916",
   "edited": "2024-08-23T20:42:02",
   "edited_unixtime": "1724434922",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48193,
   "text": "нет)",
   "text_entities": [
    {
     "type": "plain",
     "text": "нет)"
    }
   ]
  },
  {
   "id": 48195,
   "type": "message",
   "date": "2024-08-23T20:42:05",
   "date_unixtime": "1724434925",
   "from": "Илья",
   "from_id": "user418093361",
   "text": "но кате +",
   "text_entities": [
    {
     "type": "plain",
     "text": "но кате +"
    }
   ]
  },
  {
   "id": 48196,
   "type": "message",
   "date": "2024-08-23T20:42:28",
   "date_unixtime": "1724434948",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48186,
   "text": [
    {
     "type": "spoiler",
     "text": "ссущие копейки"
    },
    ""
   ],
   "text_entities": [
    {
     "type": "spoiler",
     "text": "ссущие копейки"
    },
    {
     "type": "plain",
     "text": ""
    }
   ]
  },
  {
   "id": 48197,
   "type": "message",
   "date": "2024-08-23T20:42:52",
   "date_unixtime": "1724434972",
   "edited": "2024-08-23T20:43:04",
   "edited_unixtime": "1724434984",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48188,
   "text": "типичный Миша",
   "text_entities": [
    {
     "type": "plain",
     "text": "типичный Миша"
    }
   ]
  },
  {
   "id": 48198,
   "type": "message",
   "date": "2024-08-23T20:43:28",
   "date_unixtime": "1724435008",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48188,
   "text": "и вообще, прекрати смотреть мои рилсы",
   "text_entities": [
    {
     "type": "plain",
     "text": "и вообще, прекрати смотреть мои рилсы"
    }
   ]
  },
  {
   "id": 48199,
   "type": "message",
   "date": "2024-08-23T20:43:42",
   "date_unixtime": "1724435022",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "text": "Это в тиктоке было два года назад",
   "text_entities": [
    {
     "type": "plain",
     "text": "Это в тиктоке было два года назад"
    }
   ]
  },
  {
   "id": 48200,
   "type": "message",
   "date": "2024-08-23T20:43:55",
   "date_unixtime": "1724435035",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "text": "Пугапеечка?",
   "text_entities": [
    {
     "type": "plain",
     "text": "Пугапеечка?"
    }
   ]
  },
  {
   "id": 48201,
   "type": "message",
   "date": "2024-08-23T20:44:03",
   "date_unixtime": "1724435043",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48200,
   "text": "горячо",
   "text_entities": [
    {
     "type": "plain",
     "text": "горячо"
    }
   ]
  },
  {
   "id": 48202,
   "type": "message",
   "date": "2024-08-23T20:44:53",
   "date_unixtime": "1724435093",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "reply_to_message_id": 48201,
   "text": "Горячоо",
   "text_entities": [
    {
     "type": "plain",
     "text": "Горячоо"
    }
   ]
  },
  {
   "id": 48203,
   "type": "message",
   "date": "2024-08-23T20:50:43",
   "date_unixtime": "1724435443",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "text": "Дрожжекопейка",
   "text_entities": [
    {
     "type": "plain",
     "text": "Дрожжекопейка"
    }
   ]
  },
  {
   "id": 48204,
   "type": "message",
   "date": "2024-08-23T20:53:15",
   "date_unixtime": "1724435595",
   "edited": "2024-08-23T20:56:42",
   "edited_unixtime": "1724435802",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48203,
   "text": "очень горячо, представь что их много",
   "text_entities": [
    {
     "type": "plain",
     "text": "очень горячо, представь что их много"
    }
   ]
  },
  {
   "id": 48205,
   "type": "message",
   "date": "2024-08-23T20:54:31",
   "date_unixtime": "1724435671",
   "edited": "2024-08-23T20:56:45",
   "edited_unixtime": "1724435805",
   "from": "Сергей Мирзаханов",
   "from_id": "user270735108",
   "reply_to_message_id": 48204,
   "text": "Горячоо",
   "text_entities": [
    {
     "type": "plain",
     "text": "Горячоо"
    }
   ]
  },
  {
   "id": 48206,
   "type": "message",
   "date": "2024-08-23T20:57:11",
   "date_unixtime": "1724435831",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "reply_to_message_id": 48189,
   "text": "Копибэха)",
   "text_entities": [
    {
     "type": "plain",
     "text": "Копибэха)"
    }
   ]
  },
  {
   "id": 48207,
   "type": "message",
   "date": "2024-08-23T20:59:12",
   "date_unixtime": "1724435952",
   "edited": "2024-08-23T21:03:58",
   "edited_unixtime": "1724436238",
   "from": "EKaterina Zholudeva",
   "from_id": "user452693317",
   "reply_to_message_id": 48204,
   "text": "Сущие копейки?",
   "text_entities": [
    {
     "type": "plain",
     "text": "Сущие копейки?"
    }
   ]
  },
  {
   "id": 48208,
   "type": "message",
   "date": "2024-08-24T10:07:08",
   "date_unixtime": "1724483228",
   "from": "Миша Герман",
   "from_id": "user312947484",
   "text": [
    {
     "type": "link",
     "text": "https://www.instagram.com/reel/C-5OxKjuqSY/?igsh=MW9pc2twZ2psbWY4Ng=="
    }
   ],
   "text_entities": [
    {
     "type": "link",
     "text": "https://www.instagram.com/reel/C-5OxKjuqSY/?igsh=MW9pc2twZ2psbWY4Ng=="
    }
   ]
  },
  {
   "id": 48209,
   "type": "message",
   "date": "2024-08-24T10:10:20",
   "date_unixtime": "1724483420",
   "edited": "2024-08-24T10:29:46",
   "edited_unixtime": "1724484586",
   "from": "Илья",
   "from_id": "user418093361",
   "reply_to_message_id": 48208,
   "text": "прекратите смотреть мои рилсы",
   "text_entities": [
    {
     "type": "plain",
     "text": "прекратите смотреть мои рилсы"
    }
   ]
  }
 ]
}
"""

# Пример промпта для обобщения
summarization_prompt = """Перед тобой выгрузка истории сообщений из Телеграмма, попробуй выделить пять основых тем из этой переписки: {text_to_summarize}"""



# Вызов метода summarize
summary, chat_llm_chain = summarizer.summarize(text_to_summarize, summarization_prompt)

# Печать результата
print("Summary:", summary)