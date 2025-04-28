const width = ref(0)
let initialized = false

export const useViewport = () => {
  if (import.meta.client && !initialized) {
    const updateWidth = () => {
      width.value = window.innerWidth
    }
    onMounted(() => {
      updateWidth()
      window.addEventListener('resize', updateWidth)
    })

    initialized = true
  }

  return { width }
}
