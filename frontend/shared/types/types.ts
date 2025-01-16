export interface PorfolioItemShort {
  id: number
  title: string
  images: (string | null)[]
  project_type: {
    name: 'Строительство домов' | 'Ремонт квартир'
  }
}

export interface PortfolioItemFull extends PorfolioItemShort {
  deadline: string
  cost: number
  square: number
  video_link: string
  video_duration: string
  articles: ({
    title: string
    body: string
  } | null)[]
}

type Video = {
  duration: string
  link: string
}

type PortfolioPost = {
  id: number
  title: string
  img_main: string
  img_result: string
  price_amount: string
  object_area: string
  work_completion_time: string
  type_of_work: string

  texts: {
    task?: string
    steps_of_work?: string[]
  }[]

  images?: string[]
  videos?: {
    overview?: Video
    others?: Video[]
  }
}

type BlogItem = {
  id: number
  title: string
  img_main: string
  text_main: string
  blocks?: {
    images?: string[]
    texts?: {
      title?: string
      items?: string[]
    }
  }[]
}
