import z from 'zod'

////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
export const TariffSchema = z.object({
  name: z.string(),
  description: z.string(),
  cost: z.string(),
  image: z.string()
})
export type Tariff = z.infer<typeof TariffSchema>
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
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

export type Contract = {
  id: number
  object_type: string
  order_type: string
  tariff: string
  amount_of_area: string
  object_location: string
  progress_of_work: {
    step: string
    finished: boolean
  }[]
  costs: {
    your_reward: number
    materials: number
    work_process: number
    [key: string]: number
  }
  client_info: {
    name: string
    phone: string
    email: string
    order_date: string
  }
  notifications: {
    type: string
    text?: string
    status: string
  }[]
  payments: {
    amount: number
    status: string
    text: string
  }[]
  documents: {
    type: string
    status: string
    text: string
  }[]
}
