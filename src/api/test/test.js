export default {
  Query: {
    test: async (_, __, { prisma }) => {
      const user = await prisma.user.findOne({
        where: {
          id: 5,
        },
      });
      console.log(user);
      return "Hello";
    },
  },
};
