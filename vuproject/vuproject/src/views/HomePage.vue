<template>
  <div class="home">
    <AppNavbar 
      :selected="selected" 
      :isLoggedIn="isLoggedIn"
      @update:selected="handleSelection"
    />
    
    <AdCarousel v-if="selected === 'featured'" />
    <FeaturedSection v-if="selected === 'featured'" />
    <CommunitySection v-if="selected === 'community'" />
    
    <LoginPopup 
      :isVisible="showAuthPopup"
      :initialMode="authMode"
      @success="handleAuthSuccess"
      @close="closeAuthPopup"
      @toggle-mode="updateAuthMode"
    />
    
    <ProfileSection v-if="selected === 'profile'" />
  </div>
</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";
import AdCarousel from "@/components/AdCarousel.vue";
import FeaturedSection from "@/components/FeaturedSection.vue";
import CommunitySection from "@/components/CommunitySection.vue";
import LoginPopup from "@/components/LoginSection.vue";
import ProfileSection from "@/components/ProfileSection.vue";

export default {
  components: {
    AppNavbar,
    AdCarousel,
    FeaturedSection,
    CommunitySection,
    LoginPopup,
    ProfileSection
  },
  data() {
    return {
      selected: "featured",
      showAuthPopup: false,
      authMode: 'login', // 'login' 或 'register'
      isLoggedIn: false
    };
  },
  methods: {
    handleSelection(option) {
      if (option === 'login') {
        this.authMode = 'login';
        this.showAuthPopup = true;
      } else if (option === 'register') {
        this.authMode = 'register';
        this.showAuthPopup = true;
      } else {
        this.selected = option;
      }
    },
    updateAuthMode(newMode) {
      this.authMode = newMode;
    },
    closeAuthPopup() {
      this.showAuthPopup = false;
      this.selected = "featured";
    },
    handleAuthSuccess() {
      this.closeAuthPopup();
      this.isLoggedIn = true;
      // 其他登录成功处理
    }
  }
};
</script>