<template>
  <div>
    <Toast />

    <!-- Button  to create a new user -->
    <Button style="margin: 20px;" label="Create User" icon="pi pi-user-plus" @click="showCreateDialog" class="p-button-success mb-3" />

    <!-- User Table -->
    <DataTable :value="users" paginator :rows="10" responsiveLayout="scroll">
      <Column field="username" header="Username">
        <template #body="slotProps">
          <Button 
            :label= "slotProps.data.username"
            variant="link" 
            @click="goToUserPage(slotProps.data._id)" 
            class="p-button-text"
          />
        </template>
      </Column>

      <Column field="roles" header="Roles">
        <template #body="slotProps">
          {{ formatRoles(slotProps.data.roles) }}
        </template>
      </Column>

      <Column field="preferences.timezone" header="Timezone" />

      <Column field="active" header="Is Active?">
        <template #body="slotProps">
          <span :class="slotProps.data.active ? 'text-green-600' : 'text-red-600'">
            {{ slotProps.data.active ? 'Yes' : 'No' }}
          </span>
        </template>
      </Column>

      <Column field="created_ts" header="Created At">
        <template #body="slotProps">
          {{ formatDate(slotProps.data.created_ts) }}
        </template>
      </Column>

      <Column field="updated_ts" header="Last Updated At">
        <template #body="slotProps">
          {{ formatDate(slotProps.data.updated_ts) }}
        </template>
      </Column>

      <Column header="Actions">
        <template #body="slotProps">
          <div class="flex gap-3">
            <Button icon="pi pi-pencil" class="p-button-rounded p-button-info" @click="editUser(slotProps.data)" style="margin-left: 10px; margin-right: 10px;" />
            <Button icon="pi pi-trash" class="p-button-rounded p-button-danger" @click="confirmDeleteUser(slotProps.data)" style="margin-left: 10px; margin-right: 10px;" />
          </div>
        </template>
      </Column>
    </DataTable>

    <!-- Create User Modal-->
    <Dialog v-model:visible="isCreateDialogVisible" header="Create User">
      <div class="flex flex-column gap-2">
        <label>Username: </label>
        <InputText style="margin-right: 10px" v-model="user.username" placeholder="Username" class="p-inputtext" />

        <label>Password: </label>
        <InputText style="margin-right: 10px" v-model="user.password" placeholder="Password" class="p-inputtext" />

        <label>Timezone: </label>
        <InputText style="margin-right: 10px" v-model="user.preferences.timezone" placeholder="Timezone" class="p-inputtext" />

        <!-- Roles Checkbox -->
        <label>Roles: </label>
        <div class="flex gap-3">
          <label for="active">Admin </label>
          <Checkbox binary style="margin-right: 10px"  v-model="user.is_user_admin" label="Admin" />
          <label for="active">Manager </label>
          <Checkbox binary style="margin-right: 10px"  v-model="user.is_user_manager" label="Manager" />
          <label for="active">Tester </label>
          <Checkbox binary style="margin-right: 10px"  v-model="user.is_user_tester" label="Tester" />
        </div>

        <label for="active">Active</label>
        <Checkbox 
          v-model="user.active" 
          binary 
          label="Active?" 
          style="margin: 10px;" 
        />
      </div>

      <template #footer>
        <Button label="Cancel" icon="pi pi-times" @click="isCreateDialogVisible = false" class="p-button-text" />
        <Button label="Save" icon="pi pi-check" @click="saveUser" class="p-button-primary" />
      </template>
    </Dialog>

    <!-- Edit User Modal -->
    <Dialog v-model:visible="isEditDialogVisible" header="Edit User">
      <div class="flex flex-column gap-2">
        <label>Username: </label>
        <InputText style="margin-right: 10px" v-model="user.username" placeholder="Username" class="p-inputtext" />

        <label>Password: </label>
        <InputText style="margin-right: 10px" v-model="user.password" placeholder="Password" class="p-inputtext" />

        <label>Timezone: </label>
        <InputText style="margin-right: 10px" v-model="user.preferences.timezone" placeholder="Timezone" class="p-inputtext" />

        <label>Roles: </label>
        <div class="flex gap-3">
          <label for="active">Admin </label>
          <Checkbox binary style="margin-right: 10px"  v-model="user.is_user_admin" label="Admin" />
          <label for="active">Manager </label>
          <Checkbox binary style="margin-right: 10px"  v-model="user.is_user_manager" label="Manager" />
          <label for="active">Tester </label>
          <Checkbox binary style="margin-right: 10px"  v-model="user.is_user_tester" label="Tester" />
        </div>

        <label for="active">Active</label>
        <Checkbox 
          v-model="user.active" 
          binary 
          label="Active?" 
          style="margin: 10px;" 
        />
      </div>

      <template #footer>
        <Button label="Cancel" icon="pi pi-times" @click="isEditDialogVisible = false" class="p-button-text" />
        <Button label="Save" icon="pi pi-check" @click="saveUser" class="p-button-primary" />
      </template>
    </Dialog>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'; 

export default {
  setup() {
    const users = ref([]); //User data
    const isCreateDialogVisible = ref(false); 
    const isEditDialogVisible = ref(false); 
    const user = ref({ preferences: {} });
    const router = useRouter();
    const toast = useToast(); 
    
    const goToUserPage = (userId) => {
      router.push(`/user/${userId}`); 
    };

    //Get all users
    const fetchUsers = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/users');
        users.value = response.data;
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to load users' });
      }
    };

    //Format roles for display
    const formatRoles = (roles) => {
      return Array.isArray(roles) && roles.length ? roles.join(', ') : 'None';
    };

    //Format date for display
    const formatDate = (timestamp) => {
      return new Date(timestamp * 1000).toLocaleDateString('pt-BR');
    };

    //Show create user dialog
    const showCreateDialog = () => {
      user.value = { preferences: {}, roles: [], active: true }; // Reseta o usuário
      isCreateDialogVisible.value = true;
    };

    //Show edit user dialog
    const editUser = (userData) => {
      user.value = { ...userData, preferences: { ...userData.preferences } }; // Clona os dados do usuário
      isEditDialogVisible.value = true;
    };

    //Confirm user deletion
    const confirmDeleteUser = async (userData) => {
      if (confirm(`Are you sure you want to delete ${userData.username}?`)) {
        try {
          await axios.delete(`http://localhost:5000/api/users/${userData._id}`);
          fetchUsers();
          toast.add({ severity: 'success', summary: 'Success', detail: 'User deleted successfully' });
        } catch (error) {
          toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete user' });
        }
      }
    };

    //Save user data (create or update)
    const saveUser = async () => {
    
      user.value.roles = [];
      if (user.value.is_user_admin) user.value.roles.push('admin');
      if (user.value.is_user_manager) user.value.roles.push('manager');
      if (user.value.is_user_tester) user.value.roles.push('tester');

      const userData = {
        username: user.value.username,
        password: user.value.password,
        active: user.value.active,
        created_ts: new Date().getTime() / 1000,
        updated_ts: new Date().getTime() / 1000,
        preferences: {
          timezone: user.value.preferences.timezone,
        },
        roles: user.value.roles,
      };

      try {
        if (user.value._id) {
          await axios.put(`http://localhost:5000/api/users/${user.value._id}`, userData);
          toast.add({ severity: 'success', summary: 'Success', detail: 'User updated successfully' });
        } else {
          await axios.post('http://localhost:5000/api/users', userData);
          toast.add({ severity: 'success', summary: 'Success', detail: 'User created successfully' });
        }
        fetchUsers();
        isCreateDialogVisible.value = false;
        isEditDialogVisible.value = false;
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to save user' });
      }
    };

    onMounted(fetchUsers);

    return {
      users,
      isCreateDialogVisible,
      isEditDialogVisible,
      user,
      fetchUsers,
      showCreateDialog,
      editUser,
      confirmDeleteUser,
      saveUser,
      formatRoles,
      formatDate,
      goToUserPage,
    };
  },
};
</script>
