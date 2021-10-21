new Vue({
  el: '#app',
  data: {
    cards: cards,
    selectedCard: -1
  },
  methods: {
    hoverCard(selectedIndex) {
      this.selectedCard = selectedIndex
      this.animateCards()
    },
    animateCards () {
      this.cards.forEach((card, index) => {
        const direction = this.calculateCardDirection(index, this.selectedCard)
        TweenMax.to(
          this.$refs[`card_${index}`], 
          0.3, 
          {x: direction * 50}
        )
      })
    },
    calculateCardDirection (cardIndex, selectedIndex) {
      if(selectedIndex === -1) {
        return 0
      }
      
      const diff = cardIndex - selectedIndex
      return diff === 0 ? 0 : diff/Math.abs(diff)
    },
    isSelected (cardIndex) {
      return this.selectedCard === cardIndex
    }
  }
})