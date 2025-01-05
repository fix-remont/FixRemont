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
