import type { Contract, Tariff } from '../types/responses'

let id = 0

export const portfolioItemsShort = [
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Строительство домов' }
  },
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Строительство домов' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Строительство домов' }
  },
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Строительство домов' }
  }
]

export const contract: Contract = {
  id: 41084,
  object_type: 'Квартира',
  order_type: 'Ремонт',
  tariff: 'Бизнес',
  amount_of_area: '124 м2',
  object_location: 'Казань, ул.Волкова 10, кв.26',
  progress_of_work: [
    {
      step: 'Подписание договора 1',
      finished: true
    },

    {
      step: 'Подписание договора 2',
      finished: true
    },
    {
      step: 'Подписание договора 2',
      finished: true
    },
    {
      step: 'Подписание договора 3',
      finished: true
    },
    {
      step: 'Подписание договора 4',
      finished: true
    },
    {
      step: 'Подписание договора 5',
      finished: true
    },
    {
      step: 'Подписание договора 6',
      finished: true
    },
    {
      step: 'Подписание договора 7',
      finished: true
    },
    {
      step: 'Подписание договора 8',
      finished: false
    },
    {
      step: 'Подписание договора 9',
      finished: false
    }
  ],
  costs: {
    your_reward: 32_000,
    materials: 2_175_000,
    work_process: 5_250_000
  },
  client_info: {
    name: 'Расулов Данис Фирдусович',
    phone: '+7 (900) 000-00-00',
    email: 'danis1980@mail.ru',
    order_date: '11.03.2024'
  },
  notifications: [
    {
      type: 'Требуется ваше подтверждение',
      status: 'red',
      text: 'Материалы для стен'
    },
    {
      type: 'Новое сообщение от менеджера',
      status: 'orange'
    }
  ],
  payments: [
    {
      amount: 240_000,
      status: 'green',
      text: 'Первый этап(60%)'
    },
    {
      amount: 80_000,
      status: 'orange',
      text: 'Первый этап(60%)'
    },
    {
      amount: 80_000,
      status: 'lightGray',
      text: 'Первый этап(60%)'
    },
    {
      amount: 80_000,
      status: 'light-gray',
      text: 'Первый этап(60%)'
    }
  ],
  documents: [
    {
      type: 'Договор',
      status: 'green',
      text: 'Подписан 10.02.2024'
    },
    {
      type: 'Договор',
      status: 'red',
      text: 'Подписан 10.02.2024'
    }
  ]
}

export const tariffs: Tariff[] = [
  {
    cost: 'Фикс',
    name: 'Базовый',
    image: '/images/home/package-comfort.png',
    description: 'описание 1'
  },
  {
    cost: 'Фикс',
    name: 'Стандарт',
    image: '/images/home/package-comfort.png',
    description: 'описание 2'
  },
  {
    cost: 'Фикс',
    name: 'Комфорт',
    image: '/images/home/package-comfort.png',
    description: 'описание 3'
  },
  {
    cost: 'Фикс',
    name: 'Бизнес',
    image: '/images/home/package-comfort.png',
    description: 'описание 4'
  }
]
