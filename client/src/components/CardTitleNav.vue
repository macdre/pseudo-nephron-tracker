<template>
  <vc-card-title color="primary" :dark="false">
  <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="6">
        <span class="body=2 vc-block align-left" style="font-size: 24px;">
            <b-link @click="$router.go(-1)">
            <font-awesome-icon style="color: white;" icon="arrow-left"/>
            </b-link>                  
        </span>
      </vc-col>
      <vc-col :span="12">
        <span class="body=2 vc-block" style="font-size: 24px;">{{ title }}</span>
      </vc-col>
      <vc-col :span="6">
        <span class="body=2 vc-block align-right" style="font-size: 24px;">
            <b-link to="/#">
            <font-awesome-icon style="color: white;" icon="home"/>
            </b-link>
        </span>
      </vc-col>            
  </vc-layout>
  </vc-card-title>
</template>

<script>
  export default {
    name: "CardTitleNav",
    props: [
      'title'
    ],
  };
</script>