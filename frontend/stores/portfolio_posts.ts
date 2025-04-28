import { useCustomFetch } from '~/composables/get-set-notify-fetch'
import { z } from 'zod'
import { revalidationResponseInMilliseconds } from '~/assets/variables'

const PortfolioPostSchema = z.object({
  id: z.number(),
  title: z.string(),
  deadline: z.string(),
  cost: z.number(),
  square: z.number(),
  video_link: z.string().nullable(),
  video_duration: z.string().nullable(),
  project_type: z.object({ name: z.string() }),
  images: z.array(z.string().nullable()),
  articles: z
    .array(
      z.object({
        title: z.string(),
        body: z.string()
      })
    )
    .nullable()
})

export type PortfolioPost = z.infer<typeof PortfolioPostSchema>

export const usePortfolioPostsStore = defineStore('portfolioPosts', () => {
  const lastRequestInMilliseconds = ref<number | null>(null)
  const items = ref<null | PortfolioPost[]>(null)
  const loading = ref(true)

  const millisecondsNow = +new Date()

  if (
    lastRequestInMilliseconds.value == null ||
    lastRequestInMilliseconds.value + revalidationResponseInMilliseconds < millisecondsNow
  ) {
    loading.value = true
    useCustomFetch({
      path: '/portfolio_posts',
      src: '/home/block_7',
      schema: z.array(PortfolioPostSchema)
    }).then(({ zodError, responseError, zodData }) => {
      loading.value = false

      if (!zodError && !responseError) {
        lastRequestInMilliseconds.value = millisecondsNow
        items.value = zodData as PortfolioPost[]
      }
    })
  }
  return { items, loading }
})
