<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">

          <vc-card-title color="primary" :dark="false">
            <span class="body=2 vc-block">Home</span>
          </vc-card-title>

          <vc-card-text>
            <vc-layout v-resize="resize" :class="['align-center', 'mx-0']" :spacing="8">

              <vc-col :span="6" xs24 sm12 md6>
                <vc-card class="elevation-6" tag="router-link" href="/treatment" style="text-decoration: none;">        
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-media class="pa-0" height="120px">
                    <vc-icon class="fas" color="primary" size="x-large" style="width: 120px; height: 120px;">fa-notes-medical</vc-icon>   
                  </vc-card-media>
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-title color="primary" :dark="false">
                    <span class="body=2 vc-block">Record Treatment</span>
                  </vc-card-title>
                </vc-card>
              </vc-col>

              <vc-col :span="6" xs24 sm12 md6>
                <vc-card class="elevation-6" tag="router-link" href="/inventory" style="text-decoration: none;">        
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-media class="pa-0" height="120px">
                    <vc-icon class="fas" color="primary" size="x-large" style="width: 120px; height: 120px;">fa-boxes</vc-icon>   
                  </vc-card-media>
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-title color="primary" :dark="false">
                    <span class="body=2 vc-block">Manage Inventory</span>
                  </vc-card-title>
                </vc-card>
              </vc-col>

              <vc-col :span="6" xs24 sm12 md6>
                <vc-card class="elevation-6" tag="router-link" href="/metrics" style="text-decoration: none;">        
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-media class="pa-0" height="120px">
                    <vc-icon class="fas" color="primary" size="x-large" style="width: 120px; height: 120px;">fa-chart-bar</vc-icon>   
                  </vc-card-media>
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-title color="primary" :dark="false">
                    <span class="body=2 vc-block">Explore Metrics</span>
                  </vc-card-title>
                </vc-card>
              </vc-col>

              <vc-col :span="6" xs24 sm12 md6>
                <vc-card class="elevation-6" tag="router-link" href="/setup" style="text-decoration: none;">        
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-media class="pa-0" height="120px">
                    <vc-icon class="fas" color="primary" size="x-large" style="width: 120px; height: 120px;">fa-cogs</vc-icon>   
                  </vc-card-media>
                  <vc-card-media class="pa-0" height="25px"/>
                  <vc-card-title color="primary" :dark="false">
                    <span class="body=2 vc-block">Configure Templates</span>
                  </vc-card-title>
                </vc-card>
              </vc-col>
 
            </vc-layout>
          </vc-card-text>
        </vc-card>
      </vc-col>
    </vc-layout>
  </b-container>

</template>

<script>
export default {
  name: "HomeContent"
};
</script>
