<template>
  <div class="user-page">
    <Toast />

    <div v-if="user">
      <h2>User Details</h2>
      
      <div class="user-info">
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Timezone:</strong> {{ user.preferences.timezone }}</p>
        <p><strong>Roles:</strong> {{ formatRoles(user.roles) }}</p>
        <p><strong>Is Active?</strong> <span :class="user.active ? 'text-green-600' : 'text-red-600'">{{ user.active ? 'Yes' : 'No' }}</span></p>
        <p><strong>Created At:</strong> {{ formatDate(user.created_ts) }}</p>
        <p><strong>Last Updated At:</strong> {{ formatDate(user.updated_ts) }}</p>
      </div>

      <div class="action-buttons">
        <Button icon="pi pi-pencil" label="Edit" class="p-button-info" @click="editUser" />
        <Button icon="pi pi-trash" label="Delete" class="p-button-danger" @click="confirmDeleteUser" />
        <Button icon="pi pi-home" label="Home" class="p-button-primary" @click="goHome" />
      </div>
    </div>

    <Dialog v-model:visible="isDialogVisible" header="Edit User">
      <div class="flex flex-column gap-2">
        <label>Username: </label>
        <InputText style="margin-right: 10px" v-model="user.username" placeholder="Username" class="p-inputtext" />

        <label>Timezone: </label>
        <InputText style="margin-right: 10px" v-model="user.preferences.timezone" placeholder="Timezone" class="p-inputtext" />

        <label>Roles: </label>
        <InputText style="margin-right: 10px" v-model="rolesString" placeholder="Enter roles separated by commas" class="p-inputtext" />

        <label for="active">Active</label>
        <Checkbox v-model="user.active" binary label="Active?" style="margin: 10px;" />
      </div>

      <template #footer>
        <Button label="Cancel" icon="pi pi-times" @click="isDialogVisible = false" class="p-button-text" />
        <Button label="Save" icon="pi pi-check" @click="saveUser" class="p-button-primary" />
      </template>
    </Dialog>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useToast } from 'primevue/usetoast';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const user = ref(null); 
    const isDialogVisible = ref(false); 
    const rolesString = ref(''); 
    const toast = useToast(); 
    const router = useRouter();
    const route = useRoute();

    const userId = route.params.id; 
    
    // Find user by ID
    const fetchUser = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/api/users/${userId}`);
        user.value = response.data;
        rolesString.value = user.value.roles.join(', '); 
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to load user' });
      }
    };

    // Format roles for display
    const formatRoles = (roles) => {
      return Array.isArray(roles) && roles.length ? roles.join(', ') : 'None';
    };

    // Format date for display
    const formatDate = (timestamp) => {
      return new Date(timestamp * 1000).toLocaleDateString('pt-BR');
    };

    // Edit user details
    const editUser = () => {
      isDialogVisible.value = true;
    };

    // Confirm user deletion
    const confirmDeleteUser = async () => {
      if (confirm(`Are you sure you want to delete ${user.value.username}?`)) {
        try {
          await axios.delete(`http://localhost:5000/api/users/${user.value._id}`);
          router.push('/users'); // Redireciona para a lista de usuários
          toast.add({ severity: 'success', summary: 'Success', detail: 'User deleted successfully' });
        } catch (error) {
          toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete user' });
        }
      }
    };

    // Save user details after editing
    const saveUser = async () => {
      user.value.roles = rolesString.value.split(',').map(role => role.trim()).filter(role => role);

      try {
        await axios.put(`http://localhost:5000/api/users/${user.value._id}`, user.value);
        toast.add({ severity: 'success', summary: 'Success', detail: 'User updated successfully' });
        isDialogVisible.value = false;
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to save user' });
      }
    };

    // Redirect to home page
    const goHome = () => {
      router.push('/');
    };

    onMounted(fetchUser);

    return {
      user,
      isDialogVisible,
      rolesString,
      fetchUser,
      formatRoles,
      formatDate,
      editUser,
      confirmDeleteUser,
      saveUser,
      goHome
    };
  }
};
</script>

<style scoped>
.user-page {
  padding: 20px;
}

.user-info {
  margin-bottom: 20px;
}

.action-buttons {
  display: flex;
  gap: 10px;
}
</style>
